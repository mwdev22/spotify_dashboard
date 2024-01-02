from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from dotenv import load_dotenv

# config, global static variables
load_dotenv()
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET') 
REDIRECT_URI = 'http://localhost:5000/auth/callback'
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

