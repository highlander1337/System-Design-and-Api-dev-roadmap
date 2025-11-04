using IoTServer.Models;
using Microsoft.AspNetCore.SignalR;

namespace IoTServer.Hubs
{
    /// <summary>
    /// SignalR Hub for real-time sensor data updates.
    /// </summary>
    public class SensorHub : Hub
    {
        // Hubs is moslty a passthrough, so no additional code is needed here for basic functionality.
        // we will call it from MqttService when new data arrives.


        // Optional: Override connection events for logging or other purposes.
        public override async Task OnConnectedAsync()
        {
            Console.WriteLine($"Client connected: {Context.ConnectionId}");
            await base.OnConnectedAsync();
        }

        public override async Task OnDisconnectedAsync(Exception? exception)
        {
            Console.WriteLine($"Client disconnected: {Context.ConnectionId}");
            await base.OnDisconnectedAsync(exception);
        }
    }
}