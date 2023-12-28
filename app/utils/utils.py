from flask import session, redirect
from datetime import datetime

def refresh():
    if datetime.now().timestamp() > session['expires_in']:
        return redirect('auth/refresh-token')

def check_token():
    if 'access_token' not in session:
        return redirect('/auth/login')
    