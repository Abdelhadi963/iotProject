# Generated by Django 5.0.2 on 2024-05-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='actuator_type',
            field=models.CharField(choices=[('thermostat', 'Thermostat'), ('humdifier', 'Humidifier')], max_length=50),
        ),
    ]