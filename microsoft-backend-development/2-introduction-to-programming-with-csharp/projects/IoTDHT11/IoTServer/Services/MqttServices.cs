using System.Text;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;
using IoTServer.Models;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using MQTTnet;
using MQTTnet.Server;
using System.Net;
using Microsoft.AspNetCore.SignalR;
using IoTServer.Hubs;

namespace IoTServer.Services
{
    public class MqttService : BackgroundService
    {
        private readonly IServiceScopeFactory _scopeFactory;
        private MqttServer? _mqttServer;

        private IHubContext<SensorHub>? _hubContext;

        public MqttService(IServiceScopeFactory scopeFactory, IHubContext<SensorHub> hubContext)
        {
            _hubContext = hubContext;
            _scopeFactory = scopeFactory;
        }

        public async Task PublishSensorDataAsync(SensorData data)
        {
            if (_hubContext != null)
            {
                await _hubContext.Clients.All.SendAsync("ReceiveSensorData", data);
            }
        }


        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            var factory = new MqttServerFactory();

            // Configure TCP endpoint
            var options = new MqttServerOptionsBuilder()
                .WithDefaultEndpoint()
                .WithDefaultEndpointPort(1883) // TCP port
                .Build();
                
            _mqttServer = factory.CreateMqttServer(options);

            // Client connected event
            _mqttServer.ClientConnectedAsync += e =>
            {
                Console.WriteLine($"[BROKER] Client connected: {e.ClientId}");
                return Task.CompletedTask;
            };

            // Client disconnected event
            _mqttServer.ClientDisconnectedAsync += e =>
            {
                Console.WriteLine($"[BROKER] Client disconnected: {e.ClientId}");
                return Task.CompletedTask;
            };

            // Message received event
            _mqttServer.InterceptingPublishAsync += async e =>
            {
                var topic = e.ApplicationMessage.Topic;
                var payload = Encoding.UTF8.GetString(e.ApplicationMessage.Payload);
                Console.WriteLine($"[BROKER] Message on topic '{topic}': {payload}");

                if (topic == "iot/sensors/data")
                {
                    try
                    {
                        var sensor = JsonSerializer.Deserialize<SensorData>(payload);
                        if (sensor != null)
                        {
                            using var scope = _scopeFactory.CreateScope();
                            var sensorService = scope.ServiceProvider.GetRequiredService<SensorDataService>();
                            await sensorService.StoreSensorDataAsync(sensor);
                        }
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"[BROKER] Failed to parse message: {ex.Message}");
                    }
                }
            };

            // Start server
            await _mqttServer.StartAsync();
            Console.WriteLine("[MQTT] Broker started on port 1883 (TCP)");

            // Keep running
            await Task.Delay(Timeout.Infinite, stoppingToken);
        }

        public override async Task StopAsync(CancellationToken cancellationToken)
        {
            if (_mqttServer != null)
            {
                var clients = (await _mqttServer.GetClientsAsync()).ToList();
                Console.WriteLine($"[MQTT] Disconnecting {clients.Count} clients...");

                foreach (var client in clients)
                {
                    await _mqttServer.DisconnectClientAsync(client.Id, new MqttServerClientDisconnectOptions
                    {
                        ReasonCode = MQTTnet.Protocol.MqttDisconnectReasonCode.NormalDisconnection
                    });
                }

                await _mqttServer.StopAsync();
                Console.WriteLine("[MQTT] Broker stopped");
            }

            await base.StopAsync(cancellationToken);
        }
    }
}
