namespace IoTServer.Models
{
    /// <summary>
    /// Represents a sensor data reading from an IoT device.
    public class SensorData
    {
        public int Id { get; set; } // Primary key
        public string DeviceId { get; set; } = string.Empty; // Device identifier
        public double TemperatureC { get; set; } // Temperature in Celsius
        public double TemperatureF => 32 + (int)(TemperatureC / 0.5556); // Temperature in Fahrenheit
        public double Humidity { get; set; } // Humidity percentage
        public DateTime Timestamp { get; set; } = DateTime.UtcNow; // Timestamp of the reading
    }
}