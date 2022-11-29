from rest_framework import serializers
from .models import *


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ["station_name", "date", "max_temperature","min_temperature","percipitation"]

class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yield
        fields = ["year","yield_val"]

class WeatherStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStats
        fields = ["station_name", "date", "avg_max_temperature","avg_min_temperature","total_percipitation"]
