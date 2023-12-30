from flask import redirect
from datetime import datetime

def refresh(session):
    if datetime.now().timestamp() > session['expires_in']:
        print('redirect')
        return redirect('/auth/refresh-token')

def check_token(session):
    if 'access_token' not in session:
        return redirect('/auth/login')
    