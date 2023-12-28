from flask import render_template
from flask import Flask,session,redirect, render_template
from utils.extenisons import db
from blueprints import profiles,auth,playlists

app = Flask(__name__)
print(__name__)
    # Register blueprints
app.register_blueprint(auth.routes.auth_bp)
app.register_blueprint(playlists.routes.playlists_bp)
app.register_blueprint(profiles.routes.profile_bp)
app.config.from_pyfile('config.py')

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
