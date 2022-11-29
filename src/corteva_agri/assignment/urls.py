from django.urls import path
from .views import *

urlpatterns = [
    path('weather/',get_weather_data, name='weather_data'),
    path('yield/',get_yield_data,name="yield_data"),
    path('weather/stats/',weather_statistics, name="weather_stats"),
]