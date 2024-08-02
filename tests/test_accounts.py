# tests/test_accounts.py

import json

def test_create_account(client):
    # Criação de uma instituição financeira
    client.post('/api/v1/financial_institutions/', json={'name': 'Bank1'})

    # Teste de criação de uma conta
    response = client.post('/api/v1/accounts/', json={
        'name': 'Account1',
        'type': 'savings',
        'balance': 1000,
        'financial_institution_id': 1
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'Account1'
    assert data['type'] == 'savings'
    assert data['balance'] == 1000

def test_get_account(client):
    # Criação de uma instituição financeira
    client.post('/api/v1/financial_institutions/', json={'name': 'Bank1'})

    # Primeiro, criar uma conta para testar a recuperação
    create_response = client.post('/api/v1/accounts/', json={
        'name': 'Account1',
        'type': 'savings',
        'balance': 1000,
        'financial_institution_id': 1
    })
    print("Create account response:", create_response.status_code, create_response.data)

    # Recuperar a conta criada
    response = client.get('/api/v1/accounts/1/')
    print("Get account response:", response.status_code, response.data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Account1'
    assert data['type'] == 'savings'
    assert data['balance'] == 1000

def test_update_account(client):
    # Criação de uma instituição financeira
    client.post('/api/v1/financial_institutions/', json={'name': 'Bank1'})

    # Primeiro, criar uma conta para testar a atualização
    client.post('/api/v1/accounts/', json={
        'name': 'Account1',
        'type': 'savings',
        'balance': 1000,
        'financial_institution_id': 1
    })
    # Atualizar a conta criada
    response = client.put('/api/v1/accounts/1/', json={
        'name': 'Updated Account',
        'type': 'current',
        'balance': 2000,
        'financial_institution_id': 1
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Updated Account'
    assert data['type'] == 'current'
    assert data['balance'] == 2000

def test_delete_account(client):
    # Criação de uma instituição financeira
    client.post('/api/v1/financial_institutions/', json={'name': 'Bank1'})

    # Primeiro, criar uma conta para testar a exclusão
    client.post('/api/v1/accounts/', json={
        'name': 'Account1',
        'type': 'savings',
        'balance': 1000,
        'financial_institution_id': 1
    })
    # Excluir a conta criada
    response = client.delete('/api/v1/accounts/1/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Account deleted'
    response = client.get('/api/v1/accounts/1/')
    assert response.status_code == 404

def test_list_accounts(client):
    # Criação de uma instituição financeira
    client.post('/api/v1/financial_institutions/', json={'name': 'Bank1'})

    # Criar algumas contas para listar
    client.post('/api/v1/accounts/', json={
        'name': 'Account1',
        'type': 'savings',
        'balance': 1000,
        'financial_institution_id': 1
    })
    client.post('/api/v1/accounts/', json={
        'name': 'Account2',
        'type': 'current',
        'balance': 2000,
        'financial_institution_id': 1
    })
    # Listar todas as contas
    response = client.get('/api/v1/accounts/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]['name'] == 'Account1'
    assert data[1]['name'] == 'Account2'
