from . import app
from app import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, API_BASE_URL

# blueprints
from app.blueprints.auth.routes import auth_bp
from app.blueprints.playlists.routes import playlists_bp

app.register_blueprint(auth_bp)
app.register_blueprint(playlists_bp)

if __name__ == '__main__':
    app.run(debug=True)
