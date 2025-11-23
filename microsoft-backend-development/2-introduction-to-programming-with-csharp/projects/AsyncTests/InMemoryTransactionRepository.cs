
    public class Transaction
    {
        public string Id { get; set; } = "";
        public decimal Amount { get; set; }
        public string Status { get; set; } = "";
        public DateTime TimestampUtc { get; set; }
    }
    
    public class InMemoryTransactionRepository
    {
        private readonly Dictionary<string, Transaction> _store = new();
    
        public Task SaveAsync(Transaction tx, CancellationToken cancellationToken)
        {
            cancellationToken.ThrowIfCancellationRequested();
            _store[tx.Id] = tx;
            return Task.CompletedTask;
        }
    
        public Task<Transaction?> GetAsync(string id, CancellationToken cancellationToken)
        {
            cancellationToken.ThrowIfCancellationRequested();
            _store.TryGetValue(id, out var tx);
            return Task.FromResult(tx);
        }
    }