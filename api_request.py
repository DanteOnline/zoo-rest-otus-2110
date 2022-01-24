import requests

response = requests.get('http://127.0.0.1:8000/kinds/')
print(response.json())

headers = {
    'Accept': 'application/json; version=2.0'
}
response = requests.get('http://127.0.0.1:8000/kinds/', headers=headers)
print(response.json())
