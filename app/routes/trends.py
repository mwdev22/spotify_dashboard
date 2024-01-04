from flask import Blueprint, session, render_template, jsonify
from app.utils.extenisons import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, API_BASE_URL

from app.utils.funcs import check_token, refresh
from requests import post, get
from urllib.parse import urlencode

trends_bp = Blueprint('trends', __name__, url_prefix='/trends')


@trends_bp.route('/')
def current_trends():

    check_token(session)   # checking if user is logged in
    refresh(session)   # refreshing token if expired

    headers = {
        'Authorization':f"Bearer {session['access_token']}"
    }

    # request params
    params = {
        'limit':5,
        'offset':0,
    }

    albums = ...

    tracks = ...

    return jsonify() # trends there