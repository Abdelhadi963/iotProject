# Generated by Django 5.0.2 on 2024-05-30 16:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actuator_type', models.CharField(choices=[('thermostat', 'THermostat'), ('humdifier', 'Humidifier')], max_length=50)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('installed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('command', models.CharField(max_length=255)),
                ('executed', models.BooleanField(default=False)),
                ('actuator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.actuator')),
            ],
        ),
        migrations.AddField(
            model_name='actuator',
            name='maison',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.maison'),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('sensor_types', models.CharField(choices=[('temperature', 'Temperature'), ('humidity', 'Humidity'), ('air quality', 'Air Quality')], max_length=50)),
                ('installed_at', models.DateTimeField(auto_now_add=True)),
                ('maison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.maison')),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('maison', models.ManyToManyField(blank=True, to='webapp.maison')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
