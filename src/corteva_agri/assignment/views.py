from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.core.paginator import Paginator


@api_view(['GET'])
def get_weather_data(request):
    weather = Weather.objects.all()
    if request.GET.get('date') is not None:
        weather = weather.filter(date=request.GET.get('date'))
    if request.GET.get('station_name') is not None:
        weather = weather.filter(station_name=request.GET.get('station_name'))
    pg = Paginator(weather, 200)
    page_number = request.GET.get('page')
    try:
        page_obj = pg.get_page(page_number)
    except EmptyPage:
        page_obj = pg.page(pg.num_pages)
    except PageNotAnInteger:
        page_obj = pg.page(1)
    serializer = WeatherSerializer(page_obj, many=True)
    return Response({'status':200,'msg':'Weather Data Fetched Successfully','weather_objs':serializer.data})

@api_view(['GET'])
def get_yield_data(request):
    yield_data = Yield.objects.all()
    pg = Paginator(yield_data, 200)
    page_number = request.GET.get('page')
    try:
        page_obj = pg.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = pg.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = pg.page(pg.num_pages)
    serializer = YieldSerializer(page_obj, many=True)
    return Response({'status':200,'msg':'Yield Data Fetched Successfully','yield':serializer.data})

@api_view(['GET'])
def weather_statistics(request):
    weather_stats = WeatherStats.objects.all()
    if request.GET.get('date') is not None:
        filter_date = request.GET.get('date')
        weather_stats=weather_stats.filter(date=filter_date)
    if request.GET.get('station_name') is not None:
        filter_station_name = request.GET.get('station_name')
        weather_stats=weather_stats.filter(station_name=filter_station_name)
    pg = Paginator(weather_stats, 200)
    page_number = request.GET.get('page')
    try:
        page_obj = pg.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = pg.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = pg.page(pg.num_pages)
    serializer = WeatherStatsSerializer(page_obj, many=True)
    return Response({'status':200,'msg':'Weather Statistics Data Fetched Successfully','weather_stats':serializer.data})





    


