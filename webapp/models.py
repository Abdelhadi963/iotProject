from django.db import models
from django.contrib.auth.models import User

class Maison(models.Model):
    key = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(max_length=255,blank=True,null=True)
    maison = models.ManyToManyField(Maison,blank=True)

    def __str__(self):
        return self.user.username
class Sensor(models.Model):
    SENSOR_TYPES = (
        ('temperature', 'DHT11'),
        ('temperature', 'DHT22'),
        ('temperature', 'DS18B20'),
        ('temperature', 'LM35'),
        ('humidity', 'DHT22'),
        ('humidity', 'HIH-4000'),
        ('humidity', 'SHT31'),
        ('air quality', 'Grove - Air Quality Sensor v1.3'),
        ('air quality', 'MQ-135'),
        ('air quality', 'CCS811'),
        ('light', 'TSL2561'),
        ('light', 'BH1750'),
        ('motion', 'PIR Sensor'),
        ('motion', 'HC-SR501'),
        ('pressure', 'BMP280'),
        ('pressure', 'BME680'),
        ('sound', 'KY-038'),
        ('sound', 'Grove - Sound Sensor'),
        ('proximity', 'VL53L0X'),
        ('proximity', 'Ultrasonic Sensor HC-SR04'),
    )
    maison = models.ForeignKey(Maison,on_delete=models.CASCADE)
    location = models.CharField(max_length=100,blank=True)
    sensor_types = models.CharField(max_length=50,choices=SENSOR_TYPES)
    installed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor_types} at {self.location} in {self.maison.name} '
class Reading(models.Model):
    sensor = models.ForeignKey(Sensor,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temp_value = models.FloatField(max_length=20)
    humidty_value = models.FloatField(max_length=20)
    airquality_value = models.FloatField(max_length=20)


    def __str__(self):
        return f"{self.sensor.sensor_types} reading at {self.timestamp}"
class Actuator(models.Model):
    ACTUATOR_TYPES = (
        ('thermostat', 'Smart Thermostat'),
        ('humidifier', 'Ultrasonic Humidifier'),
        ('humidifier', 'Evaporative Humidifier'),
        ('air conditioner', 'Smart Air Conditioner'),
        ('fan', 'Smart Ceiling Fan'),
        ('fan', 'Portable Smart Fan'),
        ('heater', 'Electric Heater'),
        ('heater', 'Radiant Heater'),
        ('light', 'Smart Bulb'),
        ('light', 'Smart LED Strip'),
        ('water valve', 'Smart Water Valve'),
        ('water valve', 'Motorized Ball Valve'),
        ('switch', 'Smart Switch'),
        ('switch', 'Relay Module'),
    )

    maison = models.ForeignKey(Maison,on_delete=models.CASCADE)
    actuator_type = models.CharField(max_length=50,choices=ACTUATOR_TYPES)
    location  = models.CharField(max_length=100,blank=True)
    installed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.actuator_type} at {self.location} in {self.maison.name}"
class Command(models.Model):
    actuator = models.ForeignKey(Actuator,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    command = models.CharField(max_length=255)
    executed = models.BooleanField(default=False)

    def __str__(self):
        return f"Command {self.command} for {self.actuator.actuator_type} at {self.timestamp}"
    


