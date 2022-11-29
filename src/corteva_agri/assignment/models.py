from tabnanny import verbose
from django.db import models

class Weather(models.Model):
    station_name = models.CharField(max_length=15)
    max_temperature = models.IntegerField()
    min_temperature = models.IntegerField()
    percipitation = models.IntegerField()
    date = models.CharField(max_length=8)
    
    class Meta:
        verbose_name = 'Weather'
        unique_together = (("station_name", "date"),)

    def __str__(self):
        return str(self.station_name)

class Yield(models.Model):
    year = models.CharField(max_length=10,unique=True)
    yield_val = models.IntegerField()
    
    def __str__(self):
        return str(self.year)

class WeatherStats(models.Model):
    station_name = models.CharField(max_length=15)
    avg_max_temperature = models.IntegerField()
    avg_min_temperature = models.IntegerField()
    total_percipitation = models.IntegerField()
    date = models.CharField(max_length=8)

    def __str__(self):
        return str(self.station_name)
