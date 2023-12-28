from flask import render_template
from flask import Flask,session,redirect, render_template

from blueprints import profiles,auth,playlists

app = Flask(__name__)

app.register_blueprint(auth.routes.auth_bp)
app.register_blueprint(playlists.routes.playlists_bp)
app.register_blueprint(profiles.routes.profile_bp)
