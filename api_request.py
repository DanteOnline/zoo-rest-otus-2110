import requests

url = 'http://127.0.0.1:8000/generic/create/'

# Проеряем CreateAPIView - OK
data = {"name": "Белый",
        "full_name": "Белый Медведь", "family": 9}
response = requests.post(url, data=data)
print(response.status_code)

url = 'http://127.0.0.1:8000/generic/list/'
response = requests.get(url)
print(response.json())

elements = filter(lambda item: item['name'] == "Белый", response.json())
last_id = next(elements)['id']

# Проверяем UpdateAPIVIew
# В конце обязательно нужен слеш
url = f'http://127.0.0.1:8000/generic/update/{last_id}/'
# put
data = {"name": "Черный",
        "full_name": "Черный Медведь", "family": 9}
response = requests.put(url, data=data)
print(response.status_code)

# patch
data = {"name": "patched"}
response = requests.patch(url, data=data)
print(response.status_code)

# Проверяем DestroyAPIView
url = f'http://127.0.0.1:8000/generic/destroy/{last_id}/'
response = requests.delete(url)
print(response.status_code)


