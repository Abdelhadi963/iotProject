import paho.mqtt.client as mqtt
from datetime import datetime
import re

broker_address = "127.0.0.1"
topic = "house/temp-humidity"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()

    data = payload.split(",")
    time_str = re.search(r'Timestamp:\s*(\d+:\d+:\d+)', payload).group(1)
    temperature_str = re.search(r'T=\s*(\d+.\d+)', payload).group(1)
    humidity_str = re.search(r'H=\s*(\d+.\d+)', payload).group(1)

    # Assuming the current date for the timestamp
    current_date = datetime.now().strftime("%m/%d/%y")
    timestamp_str = f"{current_date} {time_str}"
    timestamp = datetime.strptime(timestamp_str, "%m/%d/%y %H:%M:%S")
    
    temperature = float(temperature_str)
    humidity = float(humidity_str)

    sensor_type = "temperature" if "T=" in payload else "humidity"
    location = "INPT RABAT IOT-LAB"
    print(f"{timestamp} : {temperature} : {humidity} captured from {sensor_type}")

def mqtt_subscriber():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address)

    client.loop_forever()

mqtt_subscriber()
