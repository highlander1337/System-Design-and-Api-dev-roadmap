using System;
using System.Data;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;
using IoTServer.Data;
using IoTServer.Models;
using Microsoft.AspNetCore.Hosting.Server;
using Microsoft.AspNetCore.SignalR;


namespace IoTServer.Services
{
    /// <summary>
    /// Service to handle sensor data processing and storage.
    /// </summary>
    public class SensorDataService
    {
        private readonly IServiceScopeFactory _scopeFactory;
        private readonly IHubContext<Hubs.SensorHub> _hubContext;

        public SensorDataService(IServiceScopeFactory scopeFactory, IHubContext<Hubs.SensorHub> hubContext)
        {
            _scopeFactory = scopeFactory;
            _hubContext = hubContext;
        }
        
        public async Task StoreSensorDataAsync(SensorData data)
        {
            using var scope = _scopeFactory.CreateScope();
            var dbContext = scope.ServiceProvider.GetRequiredService<AppDbContext>();

            dbContext.SensorData.Add(data);
            await dbContext.SaveChangesAsync();

            // Notify connected clients via SignalR
            await _hubContext.Clients.All.SendAsync("ReceiveSensorData", data);
        }
    }
}