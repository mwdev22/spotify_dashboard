from app import create_app


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

    assert b'user_count' in response.get_json()
    assert b'user_count' in response.get_json()

def test_privacy(client):
    response = client.get('/privacy')
    assert response.status_code == 200
    assert b'Lorem' in response.data  