from flask import Flask

from app.routes.profiles import profile_bp
from app.routes.auth import auth_bp
from app.routes.main import main_bp
from app.routes.trends import trends_bp
from app.routes.search import search_bp

from app.utils.extenisons import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(trends_bp)
    app.register_blueprint(search_bp)


    db.init_app(app)
    migrate.init_app(app, db)


    return app