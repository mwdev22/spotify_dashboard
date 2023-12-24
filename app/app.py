from . import app

# blueprints
from app.blueprints.auth.routes import auth_bp

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)