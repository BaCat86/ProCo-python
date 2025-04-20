import requests

# Различные URL`ы
BASE_URL = "http://127.0.0.1:8000/" # URL-сервера, в дальнейшем надо будет вынести в файл конфигурации
url_sign_up = 'authorization/sign_up' #URL входа

# Функция для входа в аккаунт
def log_in(data): # Получаем data = (username, password)
    log_in_data = {"user_login": data[0],
                   "user_password": data[1]} # Данные для входа
    response = requests.get(f'{BASE_URL}{log_in_data}', json=data)
    print("JSON Response:", response.json())










# from sys import platform
# from os import system

# # Функция для очистки консоли
# def clear():
#     if platform == 'linux':
#         system('clear')
#     elif platform == 'win32':
#         system('cls')
#     elif platform == "darwin":
#         system('cls')

# # Функция для входа в существующий аккаунт
# def log_in():
#     clear()
#     print("[client][log_in] Необходимо пройти авторизацию")
#     user_login = input("[client][log_in] Пожалуйста, введите ваш логин: ")
#     user_password = input("[client][log_in] Пожалуйста, введите ваш пароль: ")
#     data = (user_login, user_password)
#     _ = (db.authorization(data), user_login)
#     return _

# # Функция для создания нового аккаунта
# def sign_up():
#     pass
