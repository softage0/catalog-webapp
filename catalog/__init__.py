import os
from flask import Flask
from flask_sslify import SSLify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base
from config import config

# Flask initialized
app = Flask(__name__)

# Force 'url_for' return https URL on Heroku
if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
    sslify = SSLify(app)

# DB session initialized
engine = create_engine(config.DB_URL)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# It must be imported after app, session declared
import views
import api_endpoints
import account

app.secret_key = 'super_secret_key'
