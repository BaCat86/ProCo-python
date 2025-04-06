from fastapi import FastAPI

app = FastAPI()

@app.get("/check")
def server_check():
    print('Проверка работы сервера от пользователя...')
    return 'Проверка работы сервера от пользователя...'

@app.get("/")
def server_priv():
    # print('Проверка работы сервера от пользователя...')
    return 'Дарова'

@app.get("/bimbim")
def server_bimbim():
    # print('Проверка работы сервера от пользователя...')
    return 'bimbim'
