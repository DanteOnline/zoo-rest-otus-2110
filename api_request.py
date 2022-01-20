import requests

url = 'http://127.0.0.1:8000/families/'

# доступно без авторизации
response = requests.get(url)
print(response.json())

# создание семейства, только админ
data = {'name': 'Кролик'}
response = requests.post(url, data=data)
print(response.status_code)
print(response.json())

# Базованя авторизация
data = {'name': 'Мышь'}
response = requests.post(url, data=data, auth=('admin', 'admin123456'))
print(response.status_code)
response_json = response.json()
print(response_json)
last_id = response_json['id']
url_delete = f'http://127.0.0.1:8000/families/{last_id}/'

response = requests.delete(url_delete, auth=('admin', 'admin123456'))
print(response.status_code)

# Проверка прав
data = {'name': 'Мышь'}
response = requests.post(url, data=data, auth=('oleg', 'admin123456'))
print(response.status_code)
response_json = response.json()
print(response_json)

# token = '25b91cd279be079b91573179280b8deb1225282c'
data = {
    'username': 'admin',
    'password': 'admin123456'
}

response = requests.post('http://127.0.0.1:8000/api-token-auth/', data=data)
print('-'*100)
print(response.status_code)
print(response.json())
token = response.json()['token']
print(token)
print('-'*100)

data = {'name': 'Пёс'}
headers = {'Authorization': f'Token {token}'}

response = requests.post(url, data=data, headers=headers)
print(response.status_code)
response_json = response.json()
print(response_json)
last_id = response_json['id']
url_delete = f'http://127.0.0.1:8000/families/{last_id}/'

response = requests.delete(url_delete, headers=headers)
print(response.status_code)
