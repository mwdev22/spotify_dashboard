from flask import Blueprint, redirect, session, request, url_for,jsonify
from requests import post
from urllib.parse import urlencode
from app.utils.extenisons import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, API_BASE_URL

from datetime import datetime

auth_bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')


@auth_bp.route('/login')
def login():

    # params for oauth with spotify
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': 'user-read-private user-read-email user-top-read playlist-read-private',  
        'response_type': 'code',
    }
    # encoding params
    auth_url = f'{AUTH_URL}?{urlencode(params)}'

    # redirect user to spotify login page, including encoded params with my app specification
    return redirect(auth_url)


@auth_bp.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    
    # callback getting code if authorization is succesfull
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
        session['expires_in'] = datetime.now().timestamp() + token_info['expires_in']


        return redirect('/')

@auth_bp.route('/logout')
def logout():
    # logout by clearing session data
    session.clear()
    return redirect(url_for('main.index'))  

@auth_bp.route('/refresh-token')
def refresh():

    if 'refresh_token' not in session:
        return redirect('/login')
    
    if datetime.now() > session['expires_in']:
        req_body = {
            'refresh_token':session['refresh_token'],
            'grant_type': 'authorization_code',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        response = post(TOKEN_URL, data=req_body)
        new_token_info = response.json()
        # setting up session with new data from refreshing token
        session['access_token'] = new_token_info['access_token']
        session['expires_in'] = datetime.now().timestamp() + new_token_info['expires_in']

    return redirect('/')