from tkinter import *
from tkinter import ttk     # подключаем пакет ttk

cou = 0



def main():
    root = Tk()     # создаем корневой объект - окно
    root.title("ProCo GUI")     # устанавливаем заголовок окна
    root.geometry("300x250")    # устанавливаем размеры окна
    root.resizable(True, True)
    label = Label(text="Чёто делаю") # создаем текстовую метку
    label.pack()    # размещаем метку в окне
    button = ttk.Button(text="Кнопочка", command=button_act)
    button.pack()

    root.mainloop()

def button_act():
    global cou
    cou += 1
    print(cou)
    label[] = f"Чёто делаю {cou}"

if __name__ == '__main__':
    main()
