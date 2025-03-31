from sys import platform
import os
import db_working as db

def clear():
    if platform == 'linux' or platform == 'linux':
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')
    elif platform == "darwin":
        os.system('cls')

def authorization():
    clear()
    print("[client][authorization]Необходимо пройти авторизацию")
    user_login = input("[client][authorization]Пожалуйста, введите ваш логин: ")
    user_password = input("[client][authorization]Пожалуйста, введите ваш пароль: ")
    data = (user_login, user_password)
    _ = (db.authorization(data), user_login)
    return _

def registration():
    clear()
    print("[client][registration]Необходимо пройти регистрацию")
    user_login = input("[client][registration]Пожалуйста, введите желаемый логин: ")
    user_password = input("[client][registration]Отлично!\nТеперь введите пароль: ")
    user_email = input("[client][registration]И на последок!\nВведите электронную почту: ")
    data = (user_login, user_password, user_email)
    db.registration(data)

def portfolio_view(local_id):
    ptf = portfolio_choice(local_id)
    data = (local_id, ptf)
    db.portfolio_view(data)

def portfolio_choice(local_id):
    ptf = db.portfolio_choice(local_id)
    print("Выберите портфолио из списка:")
    b = []
    for i in range(len(ptf)):
        b.append(ptf[i][0])
    for _ in range(len(b)):
        print(f"{_ + 1}. {b[_]}")
    a = int(input("Ваш выбор: "))
    a -= 1
    res = [ptf[a]]
    return res

def portfolio_create(local_id):
    print('Давайте заполним ваше новое портфолио!')
    name = input('Введите имя человека, на которого заполняется портфолио: ')
    data = (local_id, name)
    db.portfolio_create(data)

def attr_create(local_id):
    attr_name = input("Название аттрибута: ")
    attr_desc = input("Описание аттрибута: ")
    data = (attr_name, attr_desc, local_id)
    db.attr_create(data)

def attr_del(local_id):
    print("[client][attr_del]Выберите из списка аттрибут для удаления:")
    b = attr_view(local_id)
    a = int(input("Ваш выбор: "))
    db.attr_del(b[a - 1][2])

def attr_view(local_id):
    attr = db.attr_view(local_id)
    for _ in range(len(attr)):
        print(f"{_ + 1}. {attr[_][0]} - {attr[_][1]}")
    return attr

def ptf_attr_view(local_id):
    ptf = portfolio_choice(local_id)
    attr = db.ptf_attr_view(ptf[0][1])
    print(f"Портфолио {ptf[0][0]} имеет следующие аттрибуты:")
    print(attr)
    for _ in range(len(attr)):
        print(f"{_ + 1}. {attr[_][0][0]} - {attr[_][0][1]}")

def ptf_attr_choice(local_id):
    ptf = portfolio_choice(local_id)
    attr = db.ptf_attr_view(ptf[0][1])
    print(f"Выберите, какой атрибут у {ptf[0][0]} вы хотите изменить:")
    for _ in range(len(attr)):
        print(f"{_ + 1}. {attr[_][0][0]} - {attr[_][0][1]}")
    attr_res = int(input("Ваш выбор: "))
    return attr_res

def ptf_attr_edit(local_id):
    ptf = portfolio_choice(local_id)
    print(ptf)
    attr = ptf_attr_choice(local_id)
    print(attr)
    a = input("Значение которое вы хотите придать этому атрибуту: ")
    print(a)
    # db.ptf_attr_edit()

def ptf_attr_del():
    pass

def ptf_attr_add(local_id):
    ptf = portfolio_choice(local_id)
    print('Выберите из списка аттрибут, который хотите добавить к портфолио')
    attr = attr_view(local_id)
    attr_res = int(input("Ваш выбор: "))
    db.ptf_attr_add(ptf[0][1], attr[attr_res - 1][2])