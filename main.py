import sys
import db_working as db


def main():
    db.db_create()
    local_id = entry_menu()
    menu(local_id)

def authorization():
    print("[client][authorization]Необходимо пройти авторизацию")
    user_login = input("[client][authorization]Пожалуйста, введите ваш логин: ")
    user_password = input("[client][authorization]Пожалуйста, введите ваш пароль: ")
    data = (user_login, user_password)
    _ = db.authorization(data)
    return _

def registration():
    print("[client][registration]Необходимо пройти регистрацию")
    user_login = input("[client][registration]Пожалуйста, введите желаемый логин: ")
    user_password = input("[client][registration]Отлично!\nТеперь введите пароль: ")
    user_email = input("[client][registration]И на последок!\nВведите электронную почту: ")
    data = (user_login, user_password, user_email)
    db.registration(data)

def entry_menu():
    print("[client][entry_menu]Добро пожаловать в ProCo!\nПожалуйта, выберите из списка желаемое действие:\n1.Вход\n2.Регистрация\n3.Выход")
    menu_an = int(input("[client][entry_menu]Ваш выбор: "))
    if menu_an == 1:
        _ = authorization()
        return _
    elif menu_an == 2:
        registration()
        sys.exit()
    elif menu_an == 3:
        sys.exit()

def menu(local_id):
    print("[client][menu]С возвращением в ProCo!\nВыберите из списка действие, которое хотите сделать с портфолио:\n0. Выход\n1. Посмотреть существующее\n2. Создать новое\n3. Изменить существующее\n4. Редактировать аттрибуты.")
    menu_an = int(input("[client][menu]Ваш выбор: "))
    if menu_an == 0:
        sys.exit()
    elif menu_an == 1:
        portfolio_view(local_id)
        menu(local_id)
    elif menu_an == 2:
        portfolio_create(local_id)
        menu(local_id)
    elif menu_an == 3:
        portfolio_edit(local_id)
        menu(local_id)
    elif menu_an == 3:
        attr_menu()
        menu(local_id)

def portfolio_view(local_id):
    ptf = portfolio_choice(local_id)
    data = (local_id, ptf)
    db.portfolio_view(data)

def portfolio_create(local_id):
    print('Давайте заполним ваше новое портфолио!')
    name = input('Введите имя человека, на которого заполняется портфолио: ')
    data = (local_id, name)
    db.portfolio_create(data)

def portfolio_edit(local_id):
    pass

def portfolio_choice(local_id):
    pfs = db.portfolio_choice(local_id)
    print("Выберите портфолио из списка:")
    for _ in range(len(pfs)):
        print(f"{_+1}. {pfs[_]}")
    a = int(input("Ваш выбор: "))
    a -= 1
    return a

def attr_menu():
    print("[client][attr_menu]Выберите действие с аттрибутами из списка:\n0. Назад\n1. Создание аттрибута\n2. Удаление аттрибута\n3. Посмотреть все аттрибуты")
    menu_an = int(input("[client][attr_menu]Ваш выбор: "))
    if menu_an == 0:
        pass
    elif menu_an == 1:
        attr_create()
        attr_menu()
    elif menu_an == 2:
        attr_del()

def attr_create():
    attr_name = input("Название аттрибута: ")
    attr_desc = input("Описание аттрибута: ")
    data = (attr_name, attr_desc)
    db.attr_create(data)

def attr_del():
    pass

def attr_view():
    pass

main()