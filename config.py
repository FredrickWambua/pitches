import os

class Config:
    '''
    This is the general configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:12345@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY ='199478'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'wambuafred13@gmail.com'




class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:12345@localhost/pitches'
    

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}