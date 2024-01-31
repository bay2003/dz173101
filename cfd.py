import sqlite3

# Путь к базе данных
db_path = 'F:\\PYTHON 1023\\dz17_310124\\new_database.db'

# Создание соединения с базой данных
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Откройте и выполните SQL-скрипт из файла "rot.sql"
with open('F:\\PYTHON 1023\\dz17_310124\\rot.sql', 'r', encoding='utf-8') as sql_file:
    sql_script = sql_file.read()

cursor.executescript(sql_script)
conn.commit()

# Закройте соединение
conn.close()
