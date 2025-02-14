import paho.mqtt.client as mqtt
import sqlite3

# Define the MQTT broker details
BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "test/topic"

# Callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to MQTT broker!")
        client.subscribe(TOPIC)
        print(f"Subscribed to topic: {TOPIC}")
    else:
        print(f"Connection failed with return code {rc}")

# Callback for when a message is received
def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

    # Insert the received message into the database
    try:
        cursor = userdata['db_conn'].cursor()
        cursor.execute(
            "INSERT INTO Elevator_vibrations (topic, payload) VALUES (?, ?)",
            (msg.topic, msg.payload.decode())
        )
        userdata['db_conn'].commit()
        print("Message stored in database!")
    except Exception as e:
        print(f"Failed to store message: {e}")

# Initialize the database connection
def init_db():
    conn = sqlite3.connect('Elevator_vibrations.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Elevator_vibrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            payload TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn

# Main program
try:
    # Initialize database
    db_conn = init_db()
    print("Database initialized.")

    # Create MQTT client
    client = mqtt.Client(userdata={'db_conn': db_conn})  # Pass database connection as userdata
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to MQTT broker
    print("Connecting to broker...")
    client.connect(BROKER_ADDRESS, BROKER_PORT, 60)

    # Start MQTT loop
    client.loop_forever()
except Exception as e:
    print(f"Error: {e}")
finally:
    if db_conn:
        db_conn.close()
        print("Database connection closed.")
 