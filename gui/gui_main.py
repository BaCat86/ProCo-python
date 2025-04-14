from tkinter import *

def main():
    root = Tk()     # создаем корневой объект - окно
    root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
    root.geometry("300x250")    # устанавливаем размеры окна

    label = Label(text="Hello METANIT.COM") # создаем текстовую метку
    label.pack()    # размещаем метку в окне

    root.mainloop()

if __name__ == '__main__':
    main()
