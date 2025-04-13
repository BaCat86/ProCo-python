import requests

BASE_URL = "http://127.0.0.1:8000/"

url_sign_up = 'authorization/sign_up'

# def send_json():
#     data = {
#         "name": "Тестовый объект",
#         "description": "Это тестовое описание"
#     }
#     response = requests.post(f"{BASE_URL}/items/", json=data)
#     print("JSON Response:", response.json())

def sign_up():
    data = {
        "user_login": "123",
        "user_password": "123",
        "user_email": "123"
    }
    response = requests.get(f'{BASE_URL}{url_sign_up}', json=data)
    print("JSON Response:", response.json())

if __name__ == "__main__":
    sign_up()
