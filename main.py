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
    print(
        "[client][entry_menu]Добро пожаловать в ProCo!\nПожалуйта, выберите из списка желаемое действие:\n1.Вход\n2.Регистрация\n3.Выход")
    menu_an = int(input("[client][entry_menu]Ваш выбор: "))
    if menu_an == 1:
        _ = authorization()
        return _
    elif menu_an == 2:
        registration()
        print("Пожалуйста, перезапустите скрипт и войдите в аккаунт")
        sys.exit()
    elif menu_an == 3:
        sys.exit()

def menu(local_id):
    print(
        "[client][menu]С возвращением в ProCo!\nВыберите из списка действие, которое хотите сделать с портфолио:\n0. Выход\n1. Посмотреть существующее\n2. Создать новое\n3. Изменить существующее\n4. Редактировать аттрибуты.")
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
    elif menu_an == 4:
        attr_menu(local_id)
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
    # ptf = portfolio_choice(local_id)
    print("Выберите действие с портфолио из списка:\n0.Назад\n1.Посмотреть аттрибуты портфолио\n2.Редактировать значения аттрибутов\n3.Удалить аттрибут\n4.Добавить аттрибут")
    res = int(input("Ваш выбор: "))
    if res == 0:
        pass
    elif res == 1:
        ptf_attr_view(local_id)
        portfolio_edit(local_id)
    elif res == 2:
        ptf_attr_edit()
        portfolio_edit(local_id)
    elif res == 3:
        ptf_attr_del()
        portfolio_edit(local_id)
    elif res == 4:
        ptf_attr_add(local_id)
        portfolio_edit(local_id)

def portfolio_choice(local_id):
    pfs = db.portfolio_choice(local_id)
    print("Выберите портфолио из списка:")
    for _ in range(len(pfs)):
        print(f"{_ + 1}. {pfs[_]}")
    a = int(input("Ваш выбор: "))
    a -= 1
    return a

def attr_menu(local_id):
    print(
        "[client][attr_menu]Выберите действие с аттрибутами из списка:\n0. Назад\n1. Создание аттрибута\n2. Удаление аттрибута\n3. Посмотреть все аттрибуты")
    menu_an = int(input("[client][attr_menu]Ваш выбор: "))
    if menu_an == 0:
        pass
    elif menu_an == 1:
        attr_create(local_id)
        attr_menu(local_id)
    elif menu_an == 2:
        attr_del(local_id)
        attr_menu(local_id)
    elif menu_an == 3:
        attr_view(local_id)
        attr_menu(local_id)

def attr_create(local_id):
    attr_name = input("Название аттрибута: ")
    attr_desc = input("Описание аттрибута: ")
    data = (attr_name, attr_desc, local_id)
    db.attr_create(data)

def attr_del(local_id):
    print("[client][attr_del]Выберите из списка аттрибут для удаления:")
    b = attr_view(local_id)
    a = int(input("Ваш выбор: "))
    db.attr_del(local_id, b[a - 1][2])

def attr_view(local_id):
    attr = db.attr_view(local_id)
    for _ in range(len(attr)):
        print(f"{_ + 1}. {attr[_][0]} - {attr[_][1]}")
    return attr

def ptf_attr_view(local_id):
    pass

def ptf_attr_edit():
    pass

def ptf_attr_del():
    pass

def ptf_attr_add(local_id):
    ptf = portfolio_choice(local_id)
    print('Выберите из списка аттрибут, который хотите добавить к портфолио')
    attr = attr_view(local_id)
    attr_res = int(input("Ваш выбор: "))
    db.ptf_attr_add(ptf, attr[attr_res - 1][2])

main()
