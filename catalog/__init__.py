import config
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base

app = Flask(__name__)

engine = create_engine(config.DB_URL)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# It must be imported after app, session declared
import views
import json_endpoints


app.secret_key = 'super_secret_key'
app.debug = True
