from django.contrib import admin
from .models import Maison, UserProfile, Sensor, Reading, Actuator, Command 

admin.site.register(Maison)
admin.site.register(UserProfile)
admin.site.register(Sensor)
admin.site.register(Reading)
admin.site.register(Actuator)
admin.site.register(Command)

