using Microsoft.AspNetCore.Mvc;
using IoTServer.Data;
using IoTServer.Models;
using Microsoft.EntityFrameworkCore;

namespace IoTServer.controllers
{
    /// <summary>
    /// Controller to handle sensor data API requests.
    /// </summary>
    [ApiController]
    [Route("api/[controller]")]
    public class SensorController : ControllerBase
    {
        // Dependency injection of the database context
        private readonly AppDbContext _context;

        // Constructor
        public SensorController(AppDbContext context)
        {
            _context = context;
        }

        /// <summary>
        /// Receives sensor data and stores it in the database.
        /// </summary>
        /// <param name="data"></param>
        /// <returns></returns>
        [HttpPost]
        public async Task<IActionResult> PostData([FromBody] SensorData data)
        {
            if (data == null) return BadRequest("Invalid payload.");

            _context.SensorData.Add(data);
            await _context.SaveChangesAsync();
            return Ok(new { message = "Data stored successfully." });
        }

        /// <summary>
        /// // Retrieves the most recent sensor data entries.
        /// </summary>
        /// <returns></returns>
        [HttpGet]
        public async Task<IActionResult> GetData()
        {
            // Fetch a reasonable number of recent records to limit database load
            var recentData = await _context.SensorData
                .OrderByDescending(sd => sd.Timestamp)
                .Take(1000) // optional safeguard — depends on your expected data volume
                .ToListAsync();

            // Now group in memory
            var grouped = recentData
                .GroupBy(sd => sd.DeviceId)
                .SelectMany(g => g
                    .OrderByDescending(sd => sd.Timestamp)
                    .Take(10))
                .OrderBy(sd => sd.DeviceId)
                .ThenBy(sd => sd.Timestamp)
                .ToList();

            return Ok(grouped);
        }


        // public async Task<IActionResult> GetData()
        // {
        //     var recent = await _context.SensorData
        //         .OrderByDescending(sd => sd.Timestamp)
        //         .Take(10)
        //         .ToListAsync();
        //     return Ok(recent);
        // }

    }
}