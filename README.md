# Code Challenge Template
# Project Structure
- answers (logs will be generated here)
- src  (contains Django source code)
- wx_data 
- yld_data 
- approach.txt
- README.md

# Technologies
- Language - python
- Framework - Django, Django Rest Framework
- Database - sqlite
<br>

# Steps to Run

>Create and run the virtual environment using commands: 
  ```bash
   pip install virtualenv
   virtualenv env_test
  ```
>To activate virtual environment 
  ```bash
  env_test/Scripts/activate #(in Windows) 
  source env_test/bin/activate #(in Linux and Mac) 
  ```
  
>cd src/corteva_agri/ 
> - Install all the requirements using command  
  ```bash 
  pip install -r "requirements.txt"
  ```
> - Migrate the models: <br>
  ```bash
  python manage.py makemigrations 
  python manage.py makemigrations assignment (optional)
  python manage.py migrate
  ```
> - Create superuser <br>
```bash
  python manage.py createsuperuser
```
> - Ingesting the data:<br>
  Run pytohn shell in terminal using command: 
```bash
python manage.py shell 
```
>  - Run following commands:
```python
  from assignment.ingest import ingest_weather_data, ingest_yield_data, generate_statistics_data
  ingest_weather_data()
  ingest_yield_data()
  generate_statistics_data()
```
> - Data is uploaded<br>
> - Run the python server using command: 
```bash
  python manage.py runserver
```


# API LINKS

[http://127.0.0.1:8000/admin/login/?next=/admin/](http://127.0.0.1:8000/admin/login/?next=/admin/)

[http://127.0.0.1:8000/api/weather](http://127.0.0.1:8000/api/weather)<br>
[http://127.0.0.1:8000/api/yield](http://127.0.0.1:8000/api/yield) <br>
[http://127.0.0.1:8000/api/weather/stats/](http://127.0.0.1:8000/api/weather/stats/)
[http://127.0.0.1:8000/api/weather/?page=2](http://127.0.0.1:8000/api/weather/?page=2)
[http://127.0.0.1:8000/api/weather/?date=19850101](http://127.0.0.1:8000/api/weather/?date=19850101)


# TESTING

```bash
python manage.py test
```
