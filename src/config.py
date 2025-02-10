import os

class Config:

    SECRET_KEY = os.getenv('SECRET_KEY')

class ProductionConfig(Config):

    DEBUG = False
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')
    SECRET_KEY = os.getenv('SECRET_KEY')

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'voyaexplotar281024@gmail.com'
    MAIL_PASSWORD = 'qoicnybnjfhlntmu'
    MAIL_DEFAULT_SENDER = 'voyaexplotar281024@gmail.com'


class DevelopmentConfig(Config):

    DEBUG = True
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')
    SECRET_KEY = os.getenv('SECRET_KEY')

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'voyaexplotar281024@gmail.com'
    MAIL_PASSWORD = 'qoicnybnjfhlntmu'
    MAIL_DEFAULT_SENDER = 'voyaexplotar281024@gmail.com'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}