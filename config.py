import os

# default  config
class BaseConfig(object):
    """docstring for BaseConfig"""
    DEBUG = False
    SECRET_KEY = 'development key'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    