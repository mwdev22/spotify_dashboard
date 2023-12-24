from flask import Blueprint, redirect, session, request, url_for,jsonify
from requests import post, get
from urllib.parse import urlencode
from app import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, API_BASE_URL
from datetime import datetime

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
def login():
    # params for oauth with spotify
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': 'user-read-private user-read-email',  
        'response_type': 'code',
    }
    # encoding params
    auth_url = f'{AUTH_URL}?{urlencode(params)}'
    
    # redirect user to spotify login page
    return redirect(auth_url)


@auth_bp.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    if 'code' in request.args:
        code = request.args.get('code')

        req_body = {
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'grant_type': 'authorization_code',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        response = post(TOKEN_URL, data=req_body)
        token_info = response.json()
    #   to sending requests
        session['access_token'] = token_info['access_token']
    #   refreshing access token if expires
        session['refresh_token'] = token_info['refresh_token']
    #   info about expiring time
        session['expires_at'] = datetime.now() + token_info['expires_token']

        return redirect('/accounts/profile')

@auth_bp.route('/logout')
def logout():
    # clearing session data to logout
    session.clear()
    return redirect(url_for('app.home'))  

@auth_bp.route('/refresh-token')
def refresh():
    pass
