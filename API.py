from fastapi import FastAPI
import paho.mqtt.client as mqtt

import threading

app = FastAPI()

# Store received data
iot_data = {}

# MQTT Configuration
MQTT_BROKER = "localhost"  # Change to your broker's IP/hostname
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensor"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker!")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    global iot_data
    iot_data = {"topic": msg.topic, "payload": msg.payload.decode()}
    print(f"Received: {iot_data}")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Run MQTT in a separate thread
def mqtt_loop():
    mqtt_client.loop_forever()

threading.Thread(target=mqtt_loop, daemon=True).start()

# API Endpoint for React.js
@app.get("/iot-data")
async def get_iot_data():
    return iot_data
