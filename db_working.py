import sqlite3
import sys

connection = sqlite3.connect("portfolios.db")
cursor = connection.cursor()
def db_create():
    # Users
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users
    ( ID        TEXT    NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      login     TEXT    NOT NULL,
      password  TEXT    NOT NULL,
      last_seen INTEGER NULL,
      email     TEXT    NOT NULL,
      PRIMARY KEY (ID));''')
    print("[server][db_create]Создание таблицы Users - успешно")

    # Portfolios
    cursor.execute('''CREATE TABLE IF NOT EXISTS Portfolios
    ( -- ID портфолио
      ID       TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- ID пользователя
      userID   TEXT NOT NULL,
      -- Имя портфолио
      Name     TEXT NOT NULL,
      -- изображение портфолио
      pictures TEXT NULL    ,
      PRIMARY KEY (ID),
      FOREIGN KEY (userID) REFERENCES Users (ID));''')
    print("[server][db_create]Создание таблицы Portfolios - успешно")

    # Tags
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tags
    ( -- ID тэга
      ID   TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- Что за тэг
      Name TEXT NOT NULL,
      PRIMARY KEY (ID));''')
    print("[server][db_create]Создание таблицы Tags - успешно")

    # tagAssign
    cursor.execute('''CREATE TABLE IF NOT EXISTS tagAssign
    ( ID    TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- ID (связь с) портфолио
      ptfID TEXT NOT NULL,
      -- ID (связь с) тэгом
      tagID TEXT NOT NULL,
      PRIMARY KEY (ID),
      FOREIGN KEY (tagID) REFERENCES Tags (ID),
      FOREIGN KEY (ptfID) REFERENCES Portfolios (ID));''')
    print("[server][db_create]Создание таблицы tagAssign - успешно")

    # Attr
    cursor.execute('''CREATE TABLE IF NOT EXISTS Attr
    ( -- ID атрибута
      ID   TEXT NOT NULL DEFAULT (lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- имя атрибута
      Name TEXT NOT NULL,
      -- Описание атрибута
      desc TEXT NULL    ,
      PRIMARY KEY (ID));''')
    print("[server][db_create]Создание таблицы Attr - успешно")

    # value
    cursor.execute('''CREATE TABLE IF NOT EXISTS value
    ( ID    TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      value TEXT NULL    ,
      meta  TEXT NOT NULL,
      PRIMARY KEY (ID));''')
    print("[server][db_create]Создание таблицы value - успешно")

    # attrAssign
    cursor.execute('''CREATE TABLE IF NOT EXISTS attrAssign
    ( ID     TEXT    NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- ID (cвязь с) портфолио
      ptfID  TEXT    NOT NULL,
      -- ID (связь с) атрибутом
      attrID TEXT    NOT NULL,
      -- ID значения
      vID    TEXT    NOT NULL,
      -- Положение в портфолио
      orderField  INTEGER NOT NULL,
      PRIMARY KEY (ID),
      FOREIGN KEY (ptfID) REFERENCES Portfolios (ID),
      FOREIGN KEY (attrID) REFERENCES Attr (ID),
      FOREIGN KEY (vID) REFERENCES value (ID));''')
    print("[server][db_create]Создание таблицы attrAssign - успешно")

    # BaseGroup
    cursor.execute('''CREATE TABLE IF NOT EXISTS BaseGroup
    ( -- Имя группы
      groupName TEXT NOT NULL,
      -- ID пользователя
      UID       TEXT NOT NULL,
      -- ID атрибута
      AID       TEXT NOT NULL,
      PRIMARY KEY (groupName, UID, AID),
      FOREIGN KEY (UID) REFERENCES Users (ID),
      FOREIGN KEY (AID) REFERENCES Attr (ID));''')
    print("[server][db_create]Создание таблицы BaseGroup - успешно")

    connection.commit() # Изменения сохранены
    print("[server][db_create]Изменения сохранены")

def registration(data):
    cursor.execute('INSERT INTO Users (login, password, email) VALUES (?, ?, ?);', data)
    cursor.execute("SELECT * FROM Users")
    connection.commit() # Изменения сохранены
    print("[server][registration]Пользователь создан")
    print("[server][registration]Изменения сохранены")

def authorization(data):
    cursor.execute("SELECT login FROM Users")
    a = cursor.fetchall() # Перебираем, что бы получить логины в человеческом виде
    b = []
    for i in range(len(a)):
        b.append(a[i][0])
    if data[0] in b:
        print("[server][authorization]Пользователь существует!")
        cursor.execute(f"SELECT password FROM Users where login='{data[0]}'")
        a = cursor.fetchall()
        if a[0][0] == data[1]:
            cursor.execute(f"SELECT ID FROM Users where login='{data[0]}'")
            _ = cursor.fetchall()[0][0]
            print("[server][authorization]Авторизация успешна!")
            return _
        else:
            print("[server][authorization]Неверный пароль!")
            sys.exit()
    else:
        print("[server][authorization]Пользователя не существует!")
        sys.exit()

def portfolio_create(data):
    cursor.execute("INSERT INTO Portfolios (userID, Name) VALUES (?, ?)", data)
    connection.commit()
    print('Отлично, портфолио создано!')

def portfolio_choice(local_id):
    cursor.execute(f"SELECT Name FROM Portfolios where userID='{local_id}'")
    a = cursor.fetchall()
    b = []
    for i in range(len(a)):
        b.append(a[i][0])
    return b

def portfolio_view(local_id):
    print("Тут должны быть свойства портфолио, но они ищё не добавлены")

def attr_create(data):
    cursor.execute("INSERT INTO Attr (Name, desc) VALUES (?, ?)", data)
    connection.commit()
    print('Отличнео, аттрибут создан!')