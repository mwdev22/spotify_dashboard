from flask import Blueprint,session,redirect
from datetime import datetime

playlists_bp = Blueprint('playlists',__name__)

@playlists_bp.route('/')
def get_playlists():
    if 'access_token' not in session:
        return redirect('/auth/login')

    if datetime.now() > session['expires_at']:
        return redirect('auth/refresh-token')