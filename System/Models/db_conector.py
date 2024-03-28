#Import the necessary libraries
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine

#define the variables to make the conecction
driver = "mysqlconnector"
username = "root"
password = "safe&SOUND96"
server_port = "localhost"
database = "publiavisos"

#Url string of the connection
connection_string ="mysql+"+driver+"://"+username+":"+password+"@"+server_port+"/"+database

#base model of the ORM database classes
Base = declarative_base()
engine = create_engine(connection_string, echo=None)
connection = engine.connect()
session = Session(bind = engine)
