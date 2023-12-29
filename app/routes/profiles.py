from flask import Blueprint, session, render_template
from app.utils.extenisons import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, API_BASE_URL

from app.utils.funcs import check_token, refresh
from requests import post, get

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

@profile_bp.route('/')
def user_profile():
    
    check_token()   # checking if user is logged in
    refresh()   # refreshing token if expired

    headers = {
        'Authorization':f"Bearer {session['access_token']}"
    }
    response = get(f'{API_BASE_URL}me', headers=headers)
    profile = response.json()

    return render_template('profile/me.html', profile=profile)

