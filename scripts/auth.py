import requests

def auth(username, password):
    token = ''

    data = {
        'login': username,
        'password': password
    }

    auth_response = requests.post(
        'http://localhost:8080/Plone/@login', 
        headers={'Accept': 'application/json', 'Content-Type': 'application/json'}, 
        json=data)

    if auth_response.status_code == 200:
        print('Login realizado com sucesso!')
        token = auth_response.json()['token']
    else:
        print('Falha ao realizar login!')
        print(auth_response.json())

    return token

def refresh(token):
    refresh_response = requests.post(
        'http://localhost:8080/Plone/@login-renew', 
        headers={
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        })
    if refresh_response.status_code == 200:
        print('Token renovado com sucesso!')
        token = refresh_response.json()['token']
    else:
        print('Falha ao renovar token!')
        print(refresh_response.json())
    return token

def logout(token):
    logout_response = requests.post(
        'http://localhost:8080/Plone/@logout', 
        headers={
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        })
    if logout_response.status_code == 204:
        print('Logout realizado com sucesso!')
    return ''