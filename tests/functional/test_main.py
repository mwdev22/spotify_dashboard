import os
import pytest
from app import create_app

@pytest.fixture
def app():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()
    return flask_app

def test_index(app):
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        context = response.get_data(as_text=True)

        assert b'user_count' in context
        assert b'follows_average' in context

def test_privacy(app):
    with app.test_client() as client:
        response = client.get('/privacy')
        assert response.status_code == 200
        assert b'Lorem' in response.data  