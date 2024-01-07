import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

PERMANENT_SESSION_LIFETIME = timedelta(days=1)
SESSION_TYPE = 'cookie'

DEBUG = True
ENV = 'development'
