import os 

class Config:
    SECRET_KEY = "Hola esta clave"

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/tienda_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False