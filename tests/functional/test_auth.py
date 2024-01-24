from flask import session

def test_login_redirect(client):
    response = client.get('/auth/login')
    assert response.status_code == 302  

def test_callback_successful_authentication(client, mocker, session):
 
    mocker.patch('requests.post', return_value=mocker.Mock(json=lambda: {
        'access_token': 'mocked_access_token',
        'refresh_token': 'mocked_refresh_token',
        'expires_in': 3600  
    }))

    with client.session_transaction() as sess:
        sess['refresh_token'] = 'mocked_refresh_token'
        sess['expires_in'] = 3600
        sess['access_token'] = 'mocked_access_token'


    response = client.get('/auth/callback?code=mocked_code')
    

    assert response.status_code == 302
    assert session['access_token'] == 'mocked_access_token'
    assert session['refresh_token'] == 'mocked_refresh_token'
    assert 'expires_in' in session

def test_callback_error(client):
    response = client.get('/auth/callback?error=mocked_error')
    assert response.status_code == 200  
    assert 'error' in response.get_json()

def test_logout(client):
    with client.session_transaction() as sess:
        sess['access_token'] = 'mocked_access_token'
        sess['refresh_token'] = 'mocked_refresh_token'
        sess['expires_in'] = 1234567890

    response = client.get('/auth/logout')
    assert response.status_code == 302
    assert 'access_token' not in session
    assert 'refresh_token' not in session
    assert 'expires_in' not in session

def test_refresh_token(client, mocker):
    with client.session_transaction() as sess:
        sess['refresh_token'] = 'mocked_refresh_token'
        sess['expires_in'] = 0  

    mocker.patch('requests.post', return_value=mocker.Mock(json=lambda: {
        'access_token': 'mocked_new_access_token',
        'expires_in': 3600
    }))

    response = client.post('/auth/refresh-token')  
    assert response.status_code == 302
    assert 'access_token' in session
    assert 'expires_in' in session