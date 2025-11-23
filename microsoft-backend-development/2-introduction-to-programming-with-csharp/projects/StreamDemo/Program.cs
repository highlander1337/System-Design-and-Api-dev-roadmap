using System.Runtime.CompilerServices;

// Example: asynchronous stream of transactions
public class TransactionService
{
    // In real world this would call DB async streaming
    public async IAsyncEnumerable<Transaction> StreamTransactionsAsync([EnumeratorCancellation] CancellationToken ct)
    {
        for (int i = 0; i < 100; i++)
        {
            ct.ThrowIfCancellationRequested();
            await Task.Delay(50, ct).ConfigureAwait(false); // simulate IO
            yield return new Transaction { Id = i.ToString(), Amount = i, TimestampUtc = DateTime.UtcNow };
        }
    }
}

// Transaction class definition
public class Transaction
{
    public string? Id { get; set; }
    public int Amount { get; set; }
    public DateTime TimestampUtc { get; set; }
}

// Consumer
public class Program
{
    public static async Task Main(string[] args)
    {
        var service = new TransactionService();

        await foreach(var tx in service.StreamTransactionsAsync(CancellationToken.None))
        {
            Console.WriteLine($"Tx {tx.Id}: {tx.Amount}");
        }
    }
}