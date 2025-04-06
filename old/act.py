from sys import platform
import os
import sys
import db_working as db


def clear():
    if platform == 'linux':
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
    try:
        print("[client][registration]Необходимо пройти регистрацию")
        user_login = input("[client][registration]Пожалуйста, введите желаемый логин: ")
        user_password = input("[client][registration]Отлично!\nТеперь введите пароль: ")
        user_email = input("[client][registration]И на последок!\nВведите электронную почту: ")
        data = (user_login, user_password, user_email)
        db.registration(data)
    except db.sqlite3.IntegrityError as e:
        if str(e)[-11:] == 'Users.email':
            print("[server][registration]Невовозможно создать пользователя, тк почта уже занята")
        elif str(e)[-11:] == 'Users.login':
            print("[server][registration]Невовозможно создать пользователя, тк логин уже занят")
        print('Попробуйте ещё раз')
        x = input('Нажмите ENTER, что бы продолжить...')
        registration()

def portfolio_view(local_id):
    ptf = portfolio_choice(local_id)[0]
    _ = db.portfolio_view(ptf[1]) # Получу что-то вроде ([[('attrName1', 'attrDesc1')], [('attrName2', 'attrDesc2')], ..., [('attrNameN', 'attrDescN')]], [[('value1', 'meta1')], [(value2, 'meta2')], ..., [(valueN, 'metaN')]])
    if str(_) != '([], [])':
        print(f"[client][portfolio_view] Портфолио {ptf[0]} имеет следующие аттрибуты:")
        for i in range(len(_[0])):
            print(f"{i+1}. {_[0][i][0][0]} (Описание: {_[0][i][0][1]}) - {_[1][i][0][0]} (Тип значения:{_[1][i][0][1]})")
    else:
        print(f"[client][portfolio_view] Портфолио {ptf[0]} не имеет аттрибуты")
    x = input('Нажмите ENTER, что бы продолжить...')

def portfolio_choice(local_id):
    try:
        ptf = db.portfolio_choice(local_id)
        print("Для отмены нажмите ENTER...\nВыберите портфолио из списка:")
        b = []
        for i in range(len(ptf)):
            b.append(ptf[i][0])
        for _ in range(len(b)):
            print(f"{_ + 1}. {b[_]}")
        a = int(input("Ваш выбор: "))
        a -= 1
        res = [ptf[a]]
        return res # Получаем что-то вроде [('ptfName', 'ptfID')] FIX: убрать '[' и ']' в начале и конце соотвтственно, сейчас это не исправляюю тк эта переменная в слишком многих частях кода
    except IndexError:
        print('Неправильное значение портфолио, попробуйте ещё раз...')
        _ = input('Нажмите ENTER, что бы продолжить...')
        res = portfolio_choice(local_id)
        return res

def portfolio_create(local_id):
    clear()
    print('Давайте заполним ваше новое портфолио!')
    try:
        name = input('Введите имя человека, на которого заполняется портфолио: ')
        if name != '' and name.isspace() is False:
            data = (local_id, name)
            db.portfolio_create(data)
        else:
            print('Нельзя создать портфолио с пустым именем! Попробуйте ещё раз...')
            _ = input('Нажмите ENTER, что бы продолжить...')
            portfolio_create(local_id)
    except db.sqlite3.IntegrityError:
        print('Портфолио с таким именем уже существует! Попробуйте ещё раз...')
        _ = input('Нажмите ENTER, что бы продолжить...')
        portfolio_create(local_id)


def attr_create(local_id):
    try:
        attr_name = input("Название аттрибута: ")
        if attr_name != '' and attr_name.isspace() is False:
            attr_desc = input("Описание аттрибута: ")
            data = (attr_name, attr_desc, local_id)
            db.attr_create(data)
        else:
            print('Нельзя создать портфолио с пустым именем! Попробуйте ещё раз...')
            _ = input('Нажмите ENTER, что бы продолжить...')
            attr_create(local_id)
    except db.sqlite3.IntegrityError:
        print('Аттрибут с таким именем уже существует! Попробуйте ещё раз...')
        _ = input('Нажмите ENTER, что бы продолжить...')
        attr_create(local_id)

def attr_del(local_id):
    try:
        print("[client][attr_del]Выберите из списка аттрибут для удаления:")
        b = attr_view(local_id)
        a = int(input("Ваш выбор: "))
        db.attr_del(b[a - 1][2])
    except IndexError as e:
        print(str(e))
        print('Неправильное значение аттрибута, попробуйте ещё раз...')
        _ = input('Нажмите ENTER, что бы продолжить...')
        attr_del(local_id)

def attr_view(local_id):
    attr = db.attr_view(local_id)
    for _ in range(len(attr)):
        print(f"{_ + 1}. {attr[_][0]} - {attr[_][1]}")
    return attr

def ptf_attr_view(local_id):
    ptf = portfolio_choice(local_id)
    attr = db.ptf_attr_view(ptf[0][1])
    if attr != []:
        print(f"Портфолио {ptf[0][0]} имеет следующие аттрибуты:")
        for _ in range(len(attr)):
            print(f"{_ + 1}. {attr[_][0][0]} - {attr[_][0][1]}")
    else:
        print(f"Портфолио {ptf[0][0]} не имеет аттрибуты")
    _ = input('Нажмите ENTER, что бы продолжить...')

def ptf_attr_choice(local_id):
    ptf = portfolio_choice(local_id)
    attr = db.ptf_attr_view(ptf[0][1])
    print(f"Выберите, какой атрибут у {ptf[0][0]} вы хотите изменить:")
    for _ in range(len(attr)):
        print(f"{_ + 1}. {attr[_][0][0]} - {attr[_][0][1]}")
    _ = int(input("Ваш выбор: ")) - 1
    attr_res = (attr[_][0], ptf[0])

    return attr_res # Вернём что-то вроде (('attrName', 'description', 'attrID'), ('ptfName', 'ptfID'))

def ptf_attr_val_edit(local_id): # Изменение значения аттрибута
    attr = ptf_attr_choice(local_id) # Получаем, то какого аттрибут будем менять, получим что-то вроде (('attrName', 'description', 'attrID'), ('ptfName', 'ptfID'))
    print(f'Вы решили придать значение атрибуту {attr[0][0]} ({attr[0][1]})')
    attr_val = input("Значение которое вы хотите придать этому атрибуту: ") # Получаем само значение
    attr_for_edit = (attr[0][2], attr[1][1], attr_val) # Получим что-то вроде (attrID, ptfID, attr_val)
    db.ptf_attr_val_edit(attr_for_edit)

def ptf_attr_del(local_id):
    ptf = portfolio_choice(local_id) # Выбираем портфолио, у которого удалим аттрибут
    attr = db.ptf_attr_view(ptf[0][1]) # Находим все аттрибуты у портфолио
    if attr != [] and attr != [[]]: # Проверяем на наличие аттрибутов
        print(f"Какой из аттрибутов будете удалять?")
        for _ in range(len(attr)):
            print(f"{_ + 1}. {attr[_][0][0]} - {attr[_][0][1]}")
        _ = int(input("Ваш выбор: ")) - 1 # Номер нужного нам портфолио, получаем сразу значение для списка
        db.ptf_attr_del(attr[_][0][2])
    else:
        print(f"Портфолио {ptf[0][0]} не имеет аттрибуты")

def ptf_attr_add(local_id):
    ptf = portfolio_choice(local_id)
    print('Выберите из списка аттрибут, который хотите добавить к портфолио')
    attr = attr_view(local_id)
    attr_res = int(input("Ваш выбор: "))
    db.ptf_attr_add(ptf[0][1], attr[attr_res - 1][2])
