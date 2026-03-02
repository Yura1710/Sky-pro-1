import requests

LOGIN = "taraskin.yu@yandex.ru"
PASSWORD = "2807Roma"
API_URL = "https://yougile.com/api-v2"

response = requests.post(
    f"{API_URL}/auth/companies",
    json={"login": LOGIN, "password": PASSWORD}
)
print(f"Статус: {response.status_code}")
print(f"Ответ: {response.text}")
