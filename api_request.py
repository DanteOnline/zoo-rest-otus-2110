import requests


response = requests.get('http://127.0.0.1:8000/users/')
print(response.json())

response = requests.options('http://127.0.0.1:8000/users/')
print(response.json())


