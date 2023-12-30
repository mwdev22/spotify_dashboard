from flask import Blueprint, session, render_template
from app.utils.extenisons import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, API_BASE_URL

from app.utils.funcs import check_token, refresh
from requests import post, get
from urllib.parse import urlencode

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

@profile_bp.route('/')
def user_profile():
    
    check_token(session)   # checking if user is logged in
    refresh(session)   # refreshing token if expired

    # getting profile params
    headers = {
        'Authorization':f"Bearer {session['access_token']}"
    }
    prof_response = get(f'{API_BASE_URL}me', headers=headers)
    profile = prof_response.json()
    # top endpoint requires defining the scope

    artists_params = {
        'time_range':'short_term',
        'limit':5,
        'offset':0
    }

    # Update the endpoint to include the correct time_range parameter
    artists_response = get(f'{API_BASE_URL}me/top/artists?{urlencode(artists_params)}', headers=headers)
    artists = artists_response.json()

    return render_template('profile/me.html', profile=profile, artists=artists)

