import paho.mqtt.client as mqtt
import random
import time
import json

# Function to generate random BMS data
def generate_bms_data():
    return {
        "bms_id": "BMS001",
        "temperature": random.uniform(20.0, 45.0),
        "voltage": random.uniform(3.0, 4.2),
        "current": random.uniform(0.0, 10.0),
        "soc": random.randint(0, 100),
        "soh": random.randint(0, 100),
        "fan_status": random.choice(["ON", "OFF"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

# Set up MQTT client and connect to local broker
client = mqtt.Client()
client.connect("localhost", 1883)

# Publish data to topic every 5 seconds
while True:
    data = generate_bms_data()
    json_data = json.dumps(data)
    client.publish("bms/data/BMS001", json_data)
    print("Published:", json_data)
    time.sleep(5)
