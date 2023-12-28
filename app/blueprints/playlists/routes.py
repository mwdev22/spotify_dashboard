from flask import Blueprint,session,redirect, jsonify
from utils.utils import check_token, refresh
from requests import post, get
from utils.extenisons import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, API_BASE_URL

playlists_bp = Blueprint('playlists',__name__,url_prefix='/profile/playlists')

@playlists_bp.route('/')
def get_playlists():
    check_token()   # checking if user is logged in
    refresh()   # refreshing token if expired

    # getting user playlists
    headers = {
        'Authorization':f"Bearer {session['access_token']}"
    }
    response = get(f'{API_BASE_URL}/me/playlists', headers=headers)
    playlists = response.json()

    return jsonify(playlists)