# tests/integration/test_account_routes.py

def test_create_account(client):
    response = client.post('/accounts', json={'name': 'Test Account'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test Account'

def test_get_account(client):
    client.post('/accounts', json={'name': 'Test Account'})
    response = client.get('/accounts/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Test Account'

def test_update_account(client):
    client.post('/accounts', json={'name': 'Test Account'})
    response = client.put('/accounts/1', json={'name': 'Updated Account'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Updated Account'

def test_delete_account(client):
    client.post('/accounts', json={'name': 'Test Account'})
    response = client.delete('/accounts/1')
    assert response.status_code == 204
    response = client.get('/accounts/1')
    assert response.status_code == 404
