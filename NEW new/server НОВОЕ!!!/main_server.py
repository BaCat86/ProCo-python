# Всякие импорты
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import passwd_hashing as ph
import tokens


engine = create_engine("sqlite:///database.db") # Подключение к/создание бд
Base = declarative_base() # Базовый класс
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth") # Автоматический header

class User(Base): # Класс пользователя, по сути просто одна из табличек
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

Base.metadata.create_all(engine) # Создание табличек
Session = sessionmaker(bind=engine) # Создание сессии в бд
session = Session()

app = FastAPI() # Создание сессии в fastAPI

def get_db(): # Внедрение зависимостей
    db = SessionLocal()
    try:
        yield db # Типо ретёрна, но без выхода из функции
    finally:
        db.close()


@app.post("/sign_up/") # Обработка запроса А
async def signup_page(username: str, password: str, email: str):
    # if pswd == "1":
    #     response = JSONResponse({"test": "test"}, status_code=200)
    # else:
    #     response = JSONResponse({"idk": "idk"}, status_code=500)
    # if len(password) < 7:
    #     response = JSONResponse({"Error": "weak password"}, status_code=406)
    #     # ok = False
    # if session.query(User).filter(User.username == username.strip()).all():
    #     response = JSONResponse({"Error": "User already exists"}, status_code=406)
    #     ok = False
    response = {"OK": "User created"}
    try:
        hashed_paswd = ph.get_password_hash(password)
        user = User(username=username, hashed_password=hashed_paswd, email=email)
        session.add(user)
        session.commit()
    except:
        response = JSONResponse({"Error": "Cannot create user"}, status_code=406)
    return response

@app.post("/auth/")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    try:
        database_password:User = User.query().filter(User.username == username).first()
        if ph.verify_password(password, database_password)

# @app.post("/authorization/signup")
# async def return_signup_page():
#     return response


if __name__ == "__main__": # Запуск программы
    import uvicorn
    uvicorn.run("main_server:app", host="127.0.0.1", port=8000, reload=True) # Поднятие самого сервера
