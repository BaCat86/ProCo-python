from fastapi import FastAPI
from pydantic import BaseModel

import db_working as db
import act

app = FastAPI()

class Sign_up_item(BaseModel): # То, какой объет JSON мы должны получить
    user_login: str
    user_password: str
    user_email: str

# @app.post("/items/")
# async def create_item(item: Item):
#     return {
#         "message": "Данные получены (JSON)",
#         "name": item.name,
#         "description": item.description
#     }

@app.get("/ping") # Проверка, доступен ли сервер
async def ping():
    return 'The server is fine'

@app.get("/authorization/sign_up") # Регистрация нового аккаунта
async def sign_up(item: Sign_up_item):
    print('[server][sign_up] sign_up')
    print(item)
    # return 'sign_up'
    data = (item.user_login, item.user_password, item.user_email)
    try:
        db.registration(data)
        return {
            "message": "Данные получены (JSON)",
            "user_login": item.user_login,
            "user_password": item.user_password,
            "user_email": item.user_email
        }
    except db.sqlite3.IntegrityError as e:
        if str(e)[-11:] == 'Users.email':
            print("[server][registration]Невовозможно создать пользователя, тк почта уже занята")
        elif str(e)[-11:] == 'Users.login':
            print("[server][registration]Невовозможно создать пользователя, тк логин уже занят")
        print('Попробуйте ещё раз')
        return {'message': 'Ошибка при создании аккаунта'}


@app.get("/authorization/log_in") # Вход в существующий аккаунт
async def log_in():
    print('[server][log_in] log_in')
    return 'log_in'

if __name__ == "__main__":
    db.db_init()
    import uvicorn
    uvicorn.run('server:app' , host="127.0.0.1", port=8000, reload=True)
