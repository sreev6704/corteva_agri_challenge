from django.test import TestCase
from django.test.client import RequestFactory
from django.test import TestCase
from .models import *
from .views import *

class AppTestCase(TestCase):
    @classmethod
    def setUp(cls):
        Weather.objects.create(station_name="USC00257715",date="19850101",max_temperature=20,min_temperature=19,percipitation=12)
        WeatherStats.objects.create(station_name="USC00110072",date="19850101",avg_max_temperature=20,avg_min_temperature=19,total_percipitation=12)
        Yield.objects.create(year="2001",yield_val=10)
        cls.factory=RequestFactory()

    def test_weather_statistics(self):
        req=self.factory.get("/api/weather/stats/?date=19850101&&station_name=USC00110072")
        response=weather_statistics(req)
        self.assertEqual(response.data['weather_stats'][0].get("date"),"19850101")

    def test_weather_data(self):
        req=self.factory.get("/api/weather/?date=19850101&&station_name=USC00257715")
        response=get_weather_data(req)
        print("==>",response.data)
        self.assertEqual(response.data['weather_objs'][0].get("date"),"19850101")

    def test_get_yield_data(self):
        req=self.factory.get("/api/yield")
        response=get_yield_data(req)
        self.assertEqual(response.data['status'],200)
        self.assertEqual(response.data['yield'][0].get('yield_val'),10)
    
    
