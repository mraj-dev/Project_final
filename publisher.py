import paho.mqtt.client as mqtt

import time
import datetime

import random

# Define the MQTT broker details (your local Mosquitto broker)
BROKER_ADDRESS = "localhost"  # Replace with "127.0.0.1" or your computer's IP if needed
BROKER_PORT = 1883           # Default Mosquitto port
TOPIC = "test/topic"         # Replace with the topic you want to publish to

# Callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to Mosquitto broker!")
    else:
        print(f"Failed to connect, return code {rc}")

# Create an MQTT client instance
client = mqtt.Client()

# Attach the callback function
client.on_connect = on_connect

try:
    # Connect to the MQTT broker
    print("Connecting to broker...")
    client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
    
    # Start the network loop (non-blocking, required to handle connection)
    client.loop_start()

  
    while(True): 
        time_stamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        x=round(random.randint(1,10)+random.random(),2)
        y=round(random.randint(1,10)+random.random(),2)
        speed=random.randint(1,10)
        
        MESSAGE=f"{time_stamp} {x} {y} {speed}"
        time.sleep(1)
        
        client.publish(TOPIC, MESSAGE)
        print("Message published",MESSAGE)
    
    # Stop the loop after publishing
    client.loop_stop()
    client.disconnect()
    print("Message published and client disconnected.")
except Exception as e:
    print(f"Error: {e}")
