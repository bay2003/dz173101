import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('new_database.db')

# Создаем курсор
cursor = conn.cursor()

# Пример запроса: выборка данных из таблицы "Авторы"
cursor.execute('SELECT * from Авторы')

result = cursor.fetchall()
print(result)

for item in result:
    print(item)
    print(type(item))

# Пример запроса: выборка данных из таблицы "Авторы" с использованием связи
cursor.execute('SELECT * from Авторы where имя=?', ('Лев Толстой',))

print(cursor.fetchall())

# Пример запроса: вставка данных в таблицу "Книги"
cursor.execute("INSERT INTO Книги (название, id_автора, год_издания) VALUES (?, ?, ?)", ('Война и мир', 1, 1869))

# Пример запроса: выборка данных из таблицы "Книги"
cursor.execute('SELECT * from Книги')

print(cursor.fetchall())

# Пример запроса с использованием связей между таблицами
query = 'SELECT Книги.id, Авторы.имя AS автор, Книги.название AS книга, Книги.год_издания ' \
        'FROM Книги ' \
        'INNER JOIN Авторы ON Книги.id_автора = Авторы.id'

# Выполнение запроса
cursor.execute(query)

# Получение результата
result = cursor.fetchall()
for row in result:
    print(row)

# Закрытие соединения
conn.close()
