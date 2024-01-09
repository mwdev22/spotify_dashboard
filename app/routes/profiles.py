from flask import Blueprint, session, render_template, request, jsonify
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
    try:
        profile = prof_response.json()
    except:
        return jsonify({'error':'error while getting data about your spotify account'})

    # searching if user exists in our database
    existing_user = User.query.filter_by(spotify=profile['id']).first()

    if not existing_user:

        new_user = User( 
            spotify=profile['id'],
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


    # time ranges for top items offered by spotify api
    possible_ranges = {
        'in last 4 weeks':'short_term',
        'in last 6 months':'medium_term',
        'of all time':'long_term'
    }

    #   getting time range based on value from form    
    if 'time_arg' in request.args:
        time_range = possible_ranges[request.args.get('time_arg')]
    #   getting also time period to be shown on the website
        time_period = list(possible_ranges.keys())[list(possible_ranges.values()).index(time_range)]
    else:
    #   default situation, where we are opening /me endpoint for the first time
        time_period = 'in last 4 weeks'
        time_range = possible_ranges[time_period]

    #   request params for tracks and artists data
    params = {
        'time_range':time_range,
        'limit':5,
        'offset':0
    }

    # getting top tracks and artists including params
    artists_response = get(f'{API_BASE_URL}me/top/artists?{urlencode(params)}', headers=headers)
    artists = artists_response.json()['items']

    tracks_response = get(f'{API_BASE_URL}me/top/tracks?{urlencode(params)}', headers=headers)
    tracks = tracks_response.json()['items']

    return render_template('profile/me.html', profile=profile, time_period = time_period, artists=artists, tracks=tracks)

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

    return render_template('profile/my_playlists.html', playlists=playlists)