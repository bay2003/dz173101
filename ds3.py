import sqlite3

# Путь к базе данных
db_path = 'F:\\PYTHON 1023\\dz17_310124\\new_database.db'

# Создание соединения с базой данных
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQL-скрипт для создания таблиц "Авторы" и "Книги"
sql_script = """
-- Создание таблицы Авторы
CREATE TABLE Авторы (
    id INTEGER PRIMARY KEY,
    имя TEXT NOT NULL,
    страна TEXT NOT NULL
);

-- Создание таблицы Книги
CREATE TABLE Книги (
    id INTEGER PRIMARY KEY,
    название TEXT NOT NULL,
    id_автора INTEGER NOT NULL,
    год_издания INTEGER NOT NULL,
    FOREIGN KEY (id_автора) REFERENCES Авторы (id)
);

-- Добавление некоторых авторов
INSERT INTO Авторы (имя, страна) VALUES ('Лев Толстой', 'Россия');
INSERT INTO Авторы (имя, страна) VALUES ('Федор Достоевский', 'Россия');

-- Добавление некоторых книг
INSERT INTO Книги (название, id_автора, год_издания) VALUES ('Война и мир', 1, 1869);
INSERT INTO Книги (название, id_автора, год_издания) VALUES ('Анна Каренина', 1, 1877);
INSERT INTO Книги (название, id_автора, год_издания) VALUES ('Преступление и наказание', 2, 1866);
"""

# Выполнение SQL-скрипта
cursor.executescript(sql_script)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

