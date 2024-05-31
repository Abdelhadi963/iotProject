import paho.mqtt.client as mqtt
from datetime import datetime
from myapp.models import Sensor, Reading  # type: ignore # Import your Django models for sensors and readings
broker_address = "127.0.0.1"
topic = "house/temp-humidity"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    data = payload.split(",")
    timestamp_str = data[0].split(":")[1].strip()
    temperature = float(data[1].split(":")[1].strip())
    humidity = float(data[2].split(":")[1].strip())
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    sensor_type = "temperature" if "temperature" in payload else "humidity"
    location = "INPT RABAT IOT-LAB"
    sensor = Sensor.objects.get(sensor_types=sensor_type, location=location)
    reading = Reading(sensor=sensor, timestamp=timestamp, value=temperature if temperature else humidity)
    reading.save()
    print("Reading stored in the database:", reading)
def mqtt_subscriber():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address)
    client.loop_forever()
mqtt_subscriber()



