import json
import time
import paho.mqtt.client as mqtt
import random
import math

# MQTT broker configuration
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensors/data"

# MQTT client instance (initialized later)
client = None
connected = False

def connect_broker():
    global client, connected
    if connected:
        print("Already connected.")
        return

    client = mqtt.Client(client_id="MenuPublisher", protocol=mqtt.MQTTv311)
    try:
        client.connect(BROKER, PORT, keepalive=60)
        client.loop_start()  # starts background network loop
        time.sleep(1)  # wait a moment to ensure connection is established
        connected = client.is_connected()
        if connected:
            print("✅ Connected to MQTT broker")
        else:         
            print("❌ Connection failed")
        
    except Exception as e:
        connected = False
        print(f"❌ Connection failed: {e}")


def send_message():
    global client, connected

    if client is None:
        print("⚠️ You must connect first.")
        return
    
    connected = client.is_connected()

    # Check if the connection is still alive
    if not connected:
        print("⚠️ Connection lost. Reconnecting...")
        try:
            client.reconnect()
            print("✅ Reconnected to MQTT broker")
        except Exception as e:
            print(f"❌ Failed to reconnect: {e}")
            connected = False
            return

    # Prepare sample sensor data with larger deviations and spikes
    base_temp = 25
    base_humidity = 50
    # Using sine + random spikes
    temp_spike = random.choice([0, 10, 15])  # occasional big spikes
    hum_spike = random.choice([0, 15, 20])
    sensor_data = {
        "DeviceId": "esp32-01",
        "TemperatureC": round(base_temp + 10 * math.sin(time.time()) + temp_spike, 2),
        "Humidity": round(base_humidity + 10 * math.cos(time.time()) + hum_spike, 2),
        "Timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

    payload = json.dumps(sensor_data)

    # Publish the message
    result = client.publish(TOPIC, payload, qos=1)
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f"✅ Published: {payload}")
    else:
        print("❌ Failed to publish message")


def send_messages_auto(interval=1):
    print("🚀 Sending messages automatically. Press Ctrl+C to stop.")
    try:
        while True:
            send_message()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n⏹️ Automatic sending stopped by user.")

def disconnect_broker():
    global client, connected
    if not connected:
        print("⚠️  Not connected.")
        return
    client.disconnect()
    connected = False
    print("✅ Disconnected from MQTT broker")

def menu():
    while True:
        print("\nMQTT Menu:")
        print("1. Connect to broker")
        print("2. Send a message")
        print("3. Disconnect from broker")
        print("4. Send messages automatically every 1 second")
        print("5. Quit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            connect_broker()
        elif choice == "2":
            send_message()
        elif choice == "3":
            disconnect_broker()
        elif choice == "4":
            if not connected:
                print("⚠️ You must connect first.")
            else:
                send_messages_auto()
        elif choice == "5":
            if connected:
                disconnect_broker()
            print("Exiting application.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    menu()
