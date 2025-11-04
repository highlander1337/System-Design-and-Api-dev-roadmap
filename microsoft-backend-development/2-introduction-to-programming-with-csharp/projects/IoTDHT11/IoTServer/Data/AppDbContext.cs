using Microsoft.EntityFrameworkCore;
using IoTServer.Models;

namespace IoTServer.Data
{
    /// <summary>
    /// Represents the database context for the IoT server application.
    /// </summary>
    public class AppDbContext : DbContext
    {
        public DbSet<SensorData> SensorData => Set<SensorData>();

        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        /// <summary>
        /// Configures the model that was discovered by convention from the entity types
        /// exposed in DbSet properties on your derived context. The base implementation
        /// does nothing.
        /// </summary>
        /// <param name="modelBuilder"></param>
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            // Configure the SensorData entity
            base.OnModelCreating(modelBuilder);
            modelBuilder.Entity<SensorData>().ToTable("sensor_data"); // Table name
            modelBuilder.Entity<SensorData>().HasKey(sd => sd.Id); // Primary key
            modelBuilder.Entity<SensorData>().Property(sd => sd.DeviceId).IsRequired();
            modelBuilder.Entity<SensorData>().Property(sd => sd.TemperatureC).IsRequired();
            modelBuilder.Entity<SensorData>().Property(sd => sd.Humidity).IsRequired();
            modelBuilder.Entity<SensorData>().Property(sd => sd.Timestamp).IsRequired();
        }

    }
}