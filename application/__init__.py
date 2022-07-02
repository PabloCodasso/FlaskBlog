from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api


app = Flask(__name__)  # Создание экземпляра приложения
app.config.from_object(Config)  # Определение загрузки параметров конфигурации
login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application.API import UserView, UsersView

api = Api(app)  # Создание экземпляра класса для API
api.add_resource(UserView, '/APIuser/<name>')
api.add_resource(UsersView, '/APIusers')
api.init_app(app)

from application import app_routes
