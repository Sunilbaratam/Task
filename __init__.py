from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, login_manager
from flask_restful import Api
from os import path


#-----------------------initalization-------------------------
db = SQLAlchemy()
data_base = "prod.sqlite3"

#-----------------------creating app--------------------------
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisismykey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{data_base}'
    db.init_app(app)
    api = Api(app)

#---------------------adding api resources---------------------


#---------------------creating controllers---------------------
    #from .controllers import *


#----------------------importing models------------------------
    #from .models import *


#----------------------creating db-------------------------------
    #create_db(app)

#----------------------login manager-----------------------------
    
