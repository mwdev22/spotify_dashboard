from flask import Flask
from .routes.profiles import profile_bp
from .routes.auth import auth_bp
from .routes.playlists import playlists_bp
from .routes.main import main_bp
from .utils.extenisons import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(playlists_bp)
    app.register_blueprint(profile_bp)

    db.init_app(app)


    return app