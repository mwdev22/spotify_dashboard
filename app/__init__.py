from flask import Flask,session,redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import datetime

app = Flask(__name__)

# config, global static variables
load_dotenv()
app.config.from_pyfile('../config.py')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET') 
REDIRECT_URI = 'http://localhost:5000/auth/callback'
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

# database 
db = SQLAlchemy(app) 


def refresh():
    if datetime.now() > session['expires_at']:
        return redirect('auth/refresh-token')
    
def check_token():
    if 'access_token' not in session:
        return redirect('/auth/login')