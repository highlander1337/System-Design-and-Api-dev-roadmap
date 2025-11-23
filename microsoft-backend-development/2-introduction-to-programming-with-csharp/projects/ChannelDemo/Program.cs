// Program.cs - console demo for Channel producer/consumer
using System.Threading.Channels;

var channel = Channel.CreateBounded<int>(new BoundedChannelOptions(100) { FullMode = BoundedChannelFullMode.Wait });

var producer = Task.Run(async () =>
{
    var rnd = new Random();
    for (int i = 0; i < 1000; i++)
    {
        await channel.Writer.WriteAsync(rnd.Next(1000));
        await Task.Delay(5); // simulate produce rate
    }
    channel.Writer.Complete();
});

var consumer = Task.Run(async () =>
{
    await foreach (var item in channel.Reader.ReadAllAsync())
    {
        // process item (async)
        await ProcessItemAsync(item);
    }
});

await Task.WhenAll(producer, consumer);

static Task ProcessItemAsync(int item)
{
    Console.WriteLine($"Processed {item}");
    return Task.CompletedTask;
}