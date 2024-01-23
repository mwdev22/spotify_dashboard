import os
from datetime import timedelta

TESTING = True
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
PERMANENT_SESSION_LIFETIME = timedelta(days=1)
SESSION_TYPE = 'cookie'
