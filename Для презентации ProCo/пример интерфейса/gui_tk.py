# import tkinter as tk
# from tkinter import font
#
# root = tk.Tk()
# root.title("Портфолио")
# root.geometry("1200x800")
#
# # Стили шрифтов
# bold_font = font.Font(weight="bold", size=12)
# regular_font = font.Font(size=12)
# title_font = font.Font(size=14, weight="bold")
#
# # Верхняя панель с кнопками портфолио
# top_frame = tk.Frame(root)
# top_frame.pack(pady=20)
#
# for i in range(5):
#     btn_frame = tk.Frame(top_frame)
#     btn_frame.pack(side=tk.LEFT, padx=20)
#
#     tk.Label(btn_frame, text="Портфолио", font=title_font).pack()
#     tk.Label(btn_frame, text="Е", font=title_font).pack()
#
# # Основной контент
# main_frame = tk.Frame(root)
# main_frame.pack(pady=30)
#
# # Левая колонка с личной информацией
# left_frame = tk.Frame(main_frame)
# left_frame.pack(side=tk.LEFT, padx=50)
#
# info = [
#     "Имя фамилия",
#     "Отчество",
#     "Номер телефона",
#     "Почта",
#     "Дата рождения"
# ]
#
# for item in info:
#     tk.Label(left_frame, text=item, font=regular_font).pack(anchor=tk.W, pady=5)
#
# # Правая колонка с тегами
# right_frame = tk.Frame(main_frame)
# right_frame.pack(side=tk.LEFT, padx=50)
#
# tk.Label(right_frame, text="Тег 1", font=bold_font).pack(anchor=tk.W, pady=5)
# tk.Label(right_frame, text="Тег 2", font=bold_font).pack(anchor=tk.W, pady=5)
# tk.Label(right_frame, text="Тег 3", font=bold_font).pack(anchor=tk.W, pady=5)
#
# # Нижняя панель с контактами
# bottom_frame = tk.Frame(root)
# bottom_frame.pack(pady=30)
#
# contacts = [
#     ("telegram", "Описание"),
#     ("WhatsApp", "Описание")
# ]
#
# for platform, desc in contacts:
#     contact_frame = tk.Frame(bottom_frame)
#     contact_frame.pack(side=tk.LEFT, padx=30)
#
#     tk.Label(contact_frame, text=platform, font=bold_font).pack()
#     tk.Label(contact_frame, text=desc, font=regular_font).pack()
#
# root.mainloop()

import tkinter as tk

class DynamicInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Динамический интерфейс")

        # Создаем метку
        self.label = tk.Label(root, text="Введите текст и нажмите кнопку:")
        self.label.pack(pady=10)

        # Создаем текстовое поле
        self.text_input = tk.Entry(root)
        self.text_input.pack(pady=10)

        # Создаем кнопку
        self.button = tk.Button(root, text="Обновить текст", command=self.update_label)
        self.button.pack(pady=10)

    def update_label(self):
        # Обновляем текст метки
        self.label.config(text=self.text_input.get())

def main():
    root = tk.Tk()
    app = DynamicInterface(root)
    root.mainloop()

if __name__ == '__main__':
    main()
