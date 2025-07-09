import paho.mqtt.client as mqtt
import psycopg2
import json

# PostgreSQL database configuration
DB = {
    "host": "localhost" ,
    "port": 5432 ,
    "database": "BMS" ,  
    "user": "nilanazz" ,           
    "password": "1234"        
}
# MQTT settings
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "bms/data/BMS001"

# Called when the subscriber receives a message
def on_message(client, userdata, msg):
    try:
        # Decode and parse the message
        payload = msg.payload.decode()
        data = json.loads(payload)

        print("Received data:", data)

        # Connect to PostgreSQL
        conn = psycopg2.connect(**DB)
        cur = conn.cursor()

        # Insert into bms_metrics table
        insert_query = """
            INSERT INTO bms_metrics (bms_id, temperature, voltage, current, soc, soh, fan_status, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data.get("bms_id", "BMS001"),
            data["temperature"],
            data["voltage"],
            data["current"],
            data["soc"],
            data["soh"],
            data["fan_status"],
            data["timestamp"]
        )

        cur.execute(insert_query, values)
        conn.commit()

        # Close DB connection
        cur.close()
        conn.close()

    except Exception as e:
        print("Error processing message:", e)


# Set up the MQTT client
client = mqtt.Client()

# Attach the callback
client.on_message = on_message

# Connect to MQTT broker and subscribe to topic
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(MQTT_TOPIC)

print(f"Subscribed to topic: {MQTT_TOPIC}")

# Start the infinite listening loop
client.loop_forever()

