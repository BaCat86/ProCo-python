import sqlite3

connection = sqlite3.connect("portfolios.db")
cursor = connection.cursor()




def portfolio_create():
    user_id = '08d2fe55-4592-4529-85d1-56d14dda7231' # Его спокойно можно получить из таблиы, просто что бы не морочить себе голову сейчас
    print('Давайте заполним ваше первое портфолио!')
    name = input('Введите имя человека, на которого заполняется портфолио: ')
    data = (user_id, name)
    cursor.execute("INSERT INTO Portfolios (userID, Name) VALUES (?, ?)", data)
    connection.commit()
    cursor.execute("SELECT * FROM Portfolios")
    print(cursor.fetchall())
    print('Отличнео, портфолио создано!')


