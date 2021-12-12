# Flaskcode

Flask code repository

## Virtual environment

conda create -n flaskenv python=3.8
pip install -r requirements.txt

## Flask DB Migrate

a. export FLASK_APP=myapp.py
   set FLASK_APP=myapp.py

b. flask db init

c. flask db migrate -m "<messages>"

d. flask db upgrade

pip install mysqlclient
pip install psycopg2
