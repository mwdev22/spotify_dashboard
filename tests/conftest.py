import pytest
from app import create_app, db as _db
import os


@pytest.fixture
def app():
    app = create_app(config_file='../tests/config.py')
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
