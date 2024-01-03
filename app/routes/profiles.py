from flask import Blueprint, session, render_template, jsonify
from app.utils.extenisons import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, API_BASE_URL

from app.utils.funcs import check_token, refresh
from requests import post, get
from urllib.parse import urlencode
from app.models.users import User
from app.utils.extenisons import db

profile_bp = Blueprint('profile', __name__, url_prefix='/me')

@profile_bp.route('/')
def user_profile():
    
    check_token(session)   # checking if user is logged in
    refresh(session)   # refreshing token if expired

    headers = {
        'Authorization':f"Bearer {session['access_token']}"
    }
     # getting profile info
    prof_response = get(f'{API_BASE_URL}me', headers=headers)
    profile = prof_response.json()

    # searching if user exists in our database
    existing_user = User.query.filter_by(spotify_id=profile['id']).first()

    if not existing_user:

        new_user = User( 
            id=User.count_users(), # user ids based on number of users
            spotify_id=profile['id'],
            display_name=profile['display_name'],
            email=profile['email'],
            subscription=profile['product'],  
            followers=profile['followers']['total']
        )

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
    else:
        # updating user data if not logged first time
        existing_user.display_name = profile['display_name']
        existing_user.email = profile['email']
        existing_user.subscription = profile['product']
        existing_user.followers = profile['followers']['total']
        db.session.commit()
        
    print(User.count_users())
    print(User.average_followers())

    params = {
        'time_range':'short_term',
        'limit':5,
        'offset':0
    }

    # getting top tracks and artists including params
    artists_response = get(f'{API_BASE_URL}me/top/artists?{urlencode(params)}', headers=headers)
    artists = artists_response.json()

    tracks_response = get(f'{API_BASE_URL}me/top/tracks?{urlencode(params)}', headers=headers)
    tracks = tracks_response.json()

    return render_template('profile/me.html', profile=profile, artists=artists, tracks=tracks)

@profile_bp.route('/playlists')
def my_playlists():
    check_token(session)   # checking if user is logged in
    refresh(session)   # refreshing token if expired

    # getting user playlists
    headers = {
        'Authorization':f"Bearer {session['access_token']}"
    }
    response = get(f'{API_BASE_URL}me/playlists', headers=headers)
    playlists = response.json()['items']
    for playlist in playlists:
        print(playlist['name'])
    return jsonify(playlists)