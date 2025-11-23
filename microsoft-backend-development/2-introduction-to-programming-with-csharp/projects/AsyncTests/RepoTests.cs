using System.Threading;
using System.Threading.Tasks;
using Xunit;

public class RepoTests
{
    [Fact]
    public async Task SaveThenGet_ReturnsSavedTransaction()
    {
        var repo = new InMemoryTransactionRepository();
        var tx = new Transaction { Id = "tx1", Amount = 10m, Status = "OK", TimestampUtc = DateTime.UtcNow };

        await repo.SaveAsync(tx, CancellationToken.None);

        var loaded = await repo.GetAsync("tx1", CancellationToken.None);
        Assert.NotNull(loaded);
        Assert.Equal(10m, loaded!.Amount);
    }
    

    [Fact]
    public async Task CancelledSave_ThrowsOperationCanceled()
    {
        var repo = new InMemoryTransactionRepository();
        var cts = new CancellationTokenSource();
        cts.Cancel();

        await Assert.ThrowsAsync<OperationCanceledException>(() => repo.SaveAsync(new Transaction { Id = "tx2" }, cts.Token));
    }
}