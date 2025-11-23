// Program.cs (ASP.NET Core minimal API)
using System.Net.Http;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System.Threading.Channels;
using System.Threading;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<IExternalPaymentClient, ExternalPaymentClient>();
builder.Services.AddSingleton<ITransactionRepository, InMemoryTransactionRepository>();

var app = builder.Build();

app.MapPost("/pay", async (PaymentRequest req, IExternalPaymentClient paymentClient, ITransactionRepository repo, CancellationToken ct) =>
{
    // Input validation
    if (req.Amount <= 0) return Results.BadRequest("Amount must be positive");

    // Use cancellation token for timeouts / client disconnect
    var paymentResult = await paymentClient.ProcessPaymentAsync(req, ct).ConfigureAwait(false);

    if (!paymentResult.Success) return Results.StatusCode(502);

    // Persist transaction asynchronously
    var tx = new Transaction { Id = Guid.NewGuid().ToString(), Amount = req.Amount, Status = "Processed", TimestampUtc = DateTime.UtcNow };
    await repo.SaveAsync(tx, ct).ConfigureAwait(false);

    return Results.Ok(new { tx.Id });
});

app.Run();

public record PaymentRequest(decimal Amount, string AccountId);

public class Transaction { public required string Id {get; set;} public decimal Amount {get; set;} public required string Status {get; set;} public DateTime TimestampUtc {get; set;} }

public interface ITransactionRepository
{
    Task SaveAsync(Transaction t, CancellationToken ct);
    Task<Transaction?> GetAsync(string id, CancellationToken ct);
}

public class InMemoryTransactionRepository : ITransactionRepository
{
    private readonly Dictionary<string, Transaction> _store = new();
    private readonly SemaphoreSlim _mutex = new(1,1); // protect concurrent writes

    public async Task SaveAsync(Transaction t, CancellationToken ct)
    {
        await _mutex.WaitAsync(ct).ConfigureAwait(false);
        try { _store[t.Id] = t; }
        finally { _mutex.Release(); }
        await Task.CompletedTask; // placeholder for real async IO
    }

    public Task<Transaction?> GetAsync(string id, CancellationToken ct)
    {
        _store.TryGetValue(id, out var t);
        return Task.FromResult(t);
    }
}

public interface IExternalPaymentClient
{
    Task<PaymentResult> ProcessPaymentAsync(PaymentRequest req, CancellationToken ct);
}

public class PaymentResult { public bool Success {get; set;} }

public class ExternalPaymentClient : IExternalPaymentClient
{
    private readonly HttpClient _http = new HttpClient() { Timeout = TimeSpan.FromSeconds(5) };

    public async Task<PaymentResult> ProcessPaymentAsync(PaymentRequest req, CancellationToken ct)
    {
        // Simulate I/O and cancellation
        await Task.Delay(200, ct).ConfigureAwait(false);
        // In real code use _http.PostAsync(..., ct)
        return new PaymentResult { Success = true };
    }
}
