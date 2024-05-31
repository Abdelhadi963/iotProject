import paho.mqtt.client as mqtt
import time
import pandas as pd
from datetime import datetime

data = pd.read_csv("mqttserver\sensor\log_temp.csv", header=None, names=["Timestamp", "Temperature", "Humidity"])
broker_address = "127.0.0.1"
topic = "house/temp-humidity"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

def temp_humidity_sensor():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(broker_address)
    for index, row in data.iterrows():
        timestamp = row['Timestamp']
        temperature = row['Temperature']
        humidity = row['Humidity']
        # Modify payload to include timestamp
        payload = f"Timestamp: {timestamp}, Temperature: {temperature}, Humidity: {humidity}"
        client.publish(topic, payload)
        print("Published:", payload)
        time.sleep(1)
temp_humidity_sensor()


