# Всякие импорты kivy
from kivy.app import App # Базовый класс для создания приложений
from kivy.uix.boxlayout import BoxLayout # Контейнер для организации виджетов
from kivy.uix.popup import Popup # Всплывающее окно
from kivy.uix.label import Label # Текстовый элемент

from sys import exit

import act


# Класс экрана входа
class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Функция для получения значений из полей ввода
    def validate_login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        if not username or not password:
            self.show_error("Пожалуйста, заполните все поля")
        else:
            data = (username, password)
            # _ = act.log_in(data)# Проверка данных
            self.show_success(f"Добро пожаловать, {username}!")

    # Всплывающее окно ошибки
    def show_error(self, message):
        content = Label(text=message)
        popup = Popup(title="Ошибка",
                     content=content,
                     size_hint=(None, None),
                     size=(300, 200))
        popup.open()

    # Всплывающее окно успеха
    def show_success(self, message):
        content = Label(text=message)
        popup = Popup(title="Успешный вход",
                      content=content,
                      size_hint=(None, None),
                      size=(300, 200))
        popup.open()
        # Очистка полей после успешного входа
        self.ids.username.text = ""
        self.ids.password.text = ""

class LoginApp(App): # Отрисовка самого окна
    def build(self):
        return LoginScreen() # Передаём наш экран, что бы kivy его и отобразила

if __name__ == '__main__':
    LoginApp().run() # Запуск приложения
