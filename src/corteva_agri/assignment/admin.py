from django.contrib import admin
from .models import *

class WeatherAdmin(admin.ModelAdmin):
    list_display = ("station_name", "date", "max_temperature","min_temperature","percipitation")

admin.site.register(Weather, WeatherAdmin)

class YieldAdmin(admin.ModelAdmin):
    list_display = ("year","yield_val")
admin.site.register(Yield, YieldAdmin)

class WeatherStatsAdmin(admin.ModelAdmin):
    list_display = ("station_name", "date", "avg_max_temperature","avg_min_temperature","total_percipitation")
admin.site.register(WeatherStats, WeatherStatsAdmin)

