import os

class Config:
    '''
    This is the general configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:12345@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY ='199478'
    APLOADED_PHOTOS_DEST ='app/static/photos'




class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

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