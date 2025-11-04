# 🌡️ IoTServer — .NET 9 + PostgreSQL Backend

A simple ASP.NET Core Web API backend for receiving IoT sensor data (e.g., temperature and humidity) from devices like ESP32/DHT11 and storing it in a PostgreSQL database.

---

## 🚀 Features

- ASP.NET Core 9 Web API using C#
- PostgreSQL integration with Entity Framework Core (Npgsql)
- REST endpoints for posting and retrieving sensor data
- Ready for IoT devices to send JSON payloads via HTTP

---

## 🧱 Requirements

Before running this project, make sure you have:

- [.NET SDK 9.0+](https://dotnet.microsoft.com/download)
- [PostgreSQL 14+](https://www.postgresql.org/download/)
- [Visual Studio Code](https://code.visualstudio.com/) or any code editor
- `psql` CLI tool (optional, for testing database)

---

## ⚙️ Setup

1. **Clone or copy the project**

   ```bash
   git clone https://github.com/yourusername/IoTServer.git
   cd IoTServer

2. **Install dependencies**

   ```bash
   dotnet restore
   ```

3. **Update database connection string**

   Open `appsettings.json` and edit your PostgreSQL credentials:

   ```json
   "ConnectionStrings": {
     "DefaultConnection": "Host=localhost;Port=5432;Database=iotdb;Username=postgres;Password=yourpassword"
   }
   ```

4. **Install EF Core CLI (if not already installed)**

   ```bash
   dotnet tool install --global dotnet-ef
   ```

5. **Create and migrate the database**

   ```bash
   dotnet ef database update
   ```

   This will create the `iotdb` database and apply the initial migration.

---

## ▶️ Run the API

```bash
dotnet run
```

The API will start at:

```
https://localhost:7000
http://localhost:5000
```

---

## 🔌 API Endpoints

| Method | Endpoint      | Description                          |
| ------ | ------------- | ------------------------------------ |
| `POST` | `/api/sensor` | Receive IoT data in JSON format      |
| `GET`  | `/api/sensor` | Retrieve the 10 most recent readings |

### Example POST body

```json
{
  "deviceId": "esp32-01",
  "temperature": 26.5,
  "humidity": 52.3
}
```

### Example GET response

```json
[
  {
    "id": 1,
    "deviceId": "esp32-01",
    "temperature": 26.5,
    "humidity": 52.3,
    "timestamp": "2025-10-11T06:42:00Z"
  }
]
```

---

## 🧪 Test Your API

With [HTTPie](https://httpie.io/) or `curl`:

```bash
curl -X POST http://localhost:5000/api/sensor \
     -H "Content-Type: application/json" \
     -d '{"deviceId":"test","temperature":23.4,"humidity":45.1}'
```

Or check data:

```bash
curl http://localhost:5000/api/sensor
```

---

## 🛠️ Common Commands

| Command                           | Description                  |
| --------------------------------- | ---------------------------- |
| `dotnet build`                    | Compile the project          |
| `dotnet run`                      | Run the API locally          |
| `dotnet ef migrations add <Name>` | Add a new database migration |
| `dotnet ef database update`       | Apply migrations to the DB   |

---

## 🧩 Notes

* By default, EF Core uses migrations to manage schema changes.
* If you change models, run:

  ```bash
  dotnet ef migrations add UpdateModel
  dotnet ef database update
  ```
* Make sure PostgreSQL is running before starting the API.

---

## 📦 Folder Structure

```
IoTServer/
 ├── Controllers/
 │    └── SensorController.cs
 ├── Data/
 │    └── AppDbContext.cs
 ├── Models/
 │    └── SensorData.cs
 ├── appsettings.json
 ├── Program.cs
 ├── IoTServer.csproj
 └── README.md
```

---

## 💡 Next Steps

* Add authentication (JWT) to secure the API
* Connect a Blazor or React frontend
* Stream data in real-time using SignalR
* Deploy to Azure App Service or Docker

---

**🧠 Author:** Tássio Leno
**📅 Created:** October 2025
**⚙️ Tech Stack:** .NET 9, EF Core, PostgreSQL

