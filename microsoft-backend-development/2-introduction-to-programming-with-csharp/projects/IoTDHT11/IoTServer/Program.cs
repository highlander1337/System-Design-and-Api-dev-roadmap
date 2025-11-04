using IoTServer.Data;
using Microsoft.EntityFrameworkCore;
using IoTServer.Services;
using IoTServer.Hubs;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container. (Quick testing CORS policy)
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Configure PostgreSQL database connection
builder.Services.AddDbContext<AppDbContext>(options =>
{
    var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
    options.UseNpgsql(connectionString);
});

// Register application services
builder.Services.AddHostedService<MqttService>();
builder.Services.AddScoped<SensorDataService>();
builder.Services.AddSignalR();


// Add services to the container.
var app = builder.Build();

// Use CORS policy (for quick testing)
app.UseCors("AllowAll");

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// Ensure database is created
app.UseHttpsRedirection();

// Enable CORS
app.UseAuthorization();

// Map controllers
app.MapControllers();

// Map SignalR hubs
app.MapHub<SensorHub>("/sensorHub");

// Run the application
app.Run();


