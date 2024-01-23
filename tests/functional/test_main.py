from app import create_app


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    

def test_privacy(client):
    response = client.get('/privacy')
    assert response.status_code == 200
