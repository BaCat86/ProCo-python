from sys import exit

import act


# Точка старта
def main():
    local_id = entry_menu() # Меню авторизации


# Меню авторизации, возвращает токен пользователя
def entry_menu():
    print(
        "[client][entry_menu]Добро пожаловать в ProCo!\nПожалуйта, выберите из списка желаемое действие:\n--------------\n0.Выход\n1.Вход\n2.Регистрация")
    try:
        a = [1, 2, 0]
        menu_an = int(input("[client][entry_menu]Ваш выбор: "))
        if menu_an in a:
            if menu_an == 1:
                _ = act.log_in()
                print(_)
                return _
            elif menu_an == 2:
                act.sign_up()
                print("[client][entry_menu]Учётная запись успешно создана") # FIX: По хорошему сделать так, что бы не недо было перезапускать скрипт
                _ = input("Нажмите ENTER, что бы продолжить...")
                _ = entry_menu()
                return _
            elif menu_an == 0:
                exit()
        else:
            act.clear()
            print("Неккоректное значение ответа, попробуйте ещё раз...")
            _ = entry_menu()
            return _
    except ValueError:
        act.clear()
        print("Неккоректное значение ответа, попробуйте ещё раз...")
        _ = entry_menu()
        return _


if __name__ == "__main__":
    main()
