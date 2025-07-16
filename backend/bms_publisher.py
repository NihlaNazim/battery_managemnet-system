import paho.mqtt.client as mqtt
import random
import time
import json
import os

# Get MQTT broker host from environment variable (default = localhost)
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = 1883
MQTT_TOPIC = "bms/data/BMS001"

# Function to generate random BMS data
def generate_bms_data():
    return {
        "bms_id": "BMS001",
        "temperature": round(random.uniform(20.0, 45.0), 2),
        "voltage": round(random.uniform(3.0, 4.2), 2),
        "current": round(random.uniform(0.0, 10.0), 2),
        "soc": random.randint(0, 100),
        "soh": random.randint(0, 100),
        "fan_status": random.choice(["ON", "OFF"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

# Set up MQTT client and connect to the broker
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)

# Publish data to topic every 5 seconds
while True:
    data = generate_bms_data()
    json_data = json.dumps(data)
    client.publish(MQTT_TOPIC, json_data)
    print("Published:", json_data)
    time.sleep(5)
