import logging, datetime, sys, os
from assignment.models import Weather, Yield, WeatherStats

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", 
                    handlers=[logging.FileHandler(os.path.dirname(os.path.dirname(os.getcwd()))+"/answers/output.log"),logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)

def read_weather(path):
    weather = []
    for file in os.listdir():
            if file.endswith(".txt"):
                fpath = f"{path}/{file}"
                with open(fpath, "r") as data:
                    lines = [line.rstrip() for line in data]
                    for line in lines:
                        temp = line.split('\t')
                        w = Weather()
                        w.station_name = file[:-4]
                        w.date = int(temp[0])
                        w.max_temperature = int(temp[1])
                        w.min_temperature = int(temp[2])
                        w.percipitation = int(temp[3])
                        weather.append(w)
    return weather

def ingest_weather_data():
    '''
    This function is used to import the given weather data and save it to database - (sqlite db)
    '''
    path = os.path.dirname(os.path.dirname(os.getcwd()))+'/wx_data'
    print(path)
    os.chdir(path)
    start_time = datetime.datetime.now()
    logger.info("Ingestion of Weather Data Begins")
    try:
        weather=read_weather(path)
        Weather.objects.bulk_create(weather, 5000)
        end_time = datetime.datetime.now()
        logger.info("Ingestion of weather data completed successfully")
        logger.info(f"Time taken: {(end_time-start_time).total_seconds()}\t Number of rows inserted: {len(weather)}")
    except Exception as err:
        logger.error(f"{err}")
        
def ingest_yield_data():
    '''
    This function is used to import the given yield data and save it to database - (sqlite db)
    '''
    path = os.path.dirname(os.getcwd())+'/yld_data'
    print(path)
    os.chdir(path)
    logger.info("Ingestion of yield data begins")
    start_time = datetime.datetime.now()
    yieldList = []
    try:
        for file in os.listdir():
            if file.endswith(".txt"):
                fpath = f"{path}/{file}"
                with open(fpath, "r") as data:
                    lines = [line.rstrip() for line in data]
                    for line in lines:
                        temp = line.split('\t')
                        y = Yield()
                        y.year = int(temp[0])
                        y.yield_val = int(temp[1])
                        yieldList.append(y)
        Yield.objects.bulk_create(yieldList, 5000)
        end_time = datetime.datetime.now()
        logger.info("Ingestion of yield data completed successfully")
        logger.info(f"Time taken: {(end_time-start_time).total_seconds()}\t Number of rows inserted: {len(yieldList)}")
    except Exception as err:
        print(f"{err}")
    

def generate_statistics_data():
    '''
    This Function is used to compute following mathematical calculations:
    * To search for average maximum temperature 
    * To search for average minimum temperature 
    * To search for total accumulated precipitation
    for every year,for each and every every station and finally saving it into the database - (sqlite)
    '''
    datas = Weather.objects.raw("select id, station_name, date, avg(max_temperature) as max_temperature,avg(min_temperature) as min_temperature,\
                                    sum(percipitation) from (select * from assignment_weather\
                                    where max_temperature!=-9999 and min_temperature!=-9999 and percipitation!=-9999) t group by station_name , substring(date,1,4) ")
    for data in datas:
        WeatherStats.objects.get_or_create(
            station_name = data.station_name,
            date = data.date,
            avg_max_temperature = data.max_temperature,
            avg_min_temperature =data.min_temperature,
            total_percipitation = data.percipitation
            )
    print("statistics query executed succesfully")