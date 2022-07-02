import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysavestring'
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:mydatabase98@localhost:5432/Requests'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
