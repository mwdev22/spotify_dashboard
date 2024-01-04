from flask import Blueprint, session, render_template, jsonify, request
from app.utils.extenisons import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, API_BASE_URL

from app.utils.funcs import check_token, refresh
from requests import post, get
from urllib.parse import urlencode

search_bp = Blueprint('search', __name__, url_prefix='/search')

@search_bp.route('/artist/<name>')
def search_artist(name):
    artist = None
    if name in request.args:
        # request to api
        get = ...
    
    return render_template('search/artist', artist=artist)

