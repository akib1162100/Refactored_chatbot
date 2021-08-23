import locale
from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import yaml

locale.setlocale(locale.LC_TIME,locale.getlocale())

app = Flask(__name__)
db = yaml.load(open('config.yml'))

SECRET_KEY = 'soft@2019'
MYSQL_HOST = db['mysql_host']
MYSQL_USER = db['mysql_user']
MYSQL_PASSWORD= db['mysql_password']
MYSQL_DB= db['mysql_database']

mysql = MySQL(app)
database = SQLAlchemy(app)

import models
import controllers
import services
import repository