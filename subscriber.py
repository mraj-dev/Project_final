import paho.mqtt.client as mqtt
from util import *

# Define the MQTT broker details (your local Mosquitto broker)
BROKER_ADDRESS = "localhost"  # Replace with "127.0.0.1" or your computer's IP if needed
BROKER_PORT = 1883           # Default Mosquitto port
TOPIC = "test/topic"         # Replace with the topic you want to subscribe to

# Callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to Mosquitto broker!")
        # Subscribe to the topic
        client.subscribe(TOPIC)
        print(f"Subscribed to topic: {TOPIC}")
    else:
        print(f"Failed to connect, return code {rc}")

# Callback for when a message is received
def on_message(client, userdata, msg):
    add_data(msg.payload.decode())
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

# Create an MQTT client instance with the new callback API version
client = mqtt.Client()

# Attach the callback functions for the new API
client.on_connect = on_connect
client.on_message = on_message

try:
    # Connect to the MQTT broker
    print("Connecting to broker...")
    client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
    
    # Start the network loop (non-blocking)
    client.loop_forever()
except Exception as e:
    print(f"Error: {e}")