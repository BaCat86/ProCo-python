import sys
import db_working as db
import act

def main(): # Точка старта
    db.db_init() # Инициализация бд (проверка, существует ли она и если нет, то создание)
    # local_id = entry_menu()
    local_id = ('599d253c-d924-445b-b7d9-7297597b10ff', '123') # получаем что-то вроде local_id = (user_id, user_name)
    menu(local_id)

def entry_menu(): # Меню авторизации
    print(
        "[client][entry_menu]Добро пожаловать в ProCo!\nПожалуйта, выберите из списка желаемое действие:\n--------------\n0.Выход\n1.Вход\n2.Регистрация")
    menu_an = int(input("[client][entry_menu]Ваш выбор: "))
    if menu_an == 1:
        _ = act.authorization()
        print(_)
        return _
    elif menu_an == 2:
        act.registration()
        print("Пожалуйста, перезапустите скрипт и войдите в аккаунт") # FIX: По хорошему сделать так, что бы не недо было перезапускать скрипт
        sys.exit()
    elif menu_an == 0:
        sys.exit()

def menu(local_id): # Меню пользователя
    act.clear()
    print(
        f"[client][menu]С возвращением в ProCo, {local_id[1]}!\nВыберите из списка действие, которое хотите сделать с портфолио:\n--------------\n0. Выход\n1. Посмотреть существующее\n2. Создать новое\n3. Изменить существующее\n4. Редактировать аттрибуты.")
    menu_an = int(input("[client][menu]Ваш выбор: "))
    act.clear()
    if menu_an == 0:
        sys.exit()
    elif menu_an == 1:
        act.portfolio_view(local_id[0])
    elif menu_an == 2:
        act.portfolio_create(local_id[0])
    elif menu_an == 3:
        portfolio_edit_menu(local_id[0])
    elif menu_an == 4:
        attr_menu(local_id[0])
    menu(local_id)

def portfolio_edit_menu(local_id):
    print("Выберите действие с портфолио из списка:\n--------------\n0.Назад\n1.Посмотреть аттрибуты портфолио\n2.Редактировать значения аттрибутов\n3.Удалить аттрибут\n4.Добавить аттрибут")
    res = int(input("Ваш выбор: "))
    if res == 0:
        menu(local_id)
    elif res == 1:
        act.ptf_attr_view(local_id)
    elif res == 2:
        act.ptf_attr_val_edit(local_id)
    elif res == 3:
        act.ptf_attr_del(local_id)
    elif res == 4:
        act.ptf_attr_add(local_id)
    portfolio_edit_menu(local_id)

def attr_menu(local_id):
    act.clear()
    print(
        "[client][attr_menu]Выберите действие с аттрибутами из списка:\n--------------\n0. Назад\n1. Создание аттрибута\n2. Удаление аттрибута\n3. Посмотреть все аттрибуты")
    menu_an = int(input("[client][attr_menu]Ваш выбор: "))
    if menu_an == 0:
        menu(local_id)
    elif menu_an == 1:
        act.attr_create(local_id)
    elif menu_an == 2:
        act.attr_del(local_id)
    elif menu_an == 3:
        act.attr_view(local_id)
        _ = input("Нажмите ENTER, для продолжения...")
    attr_menu(local_id)

if __name__ == "__main__":
    main()
