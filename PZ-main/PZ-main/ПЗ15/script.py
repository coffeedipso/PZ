#Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для некоторой организации.
# БД должна содержать таблицу Клиент со следующей структурой записи: 
#ФИО клиента, код помещения, срок аренды, стоимость аренды за весь срок.
import sqlite3

# Создание таблицы "Клиент" если она не существует
def create_table():
    conn = sqlite3.connect('arendnayabaza.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Клиент (
            ФИО TEXT,
            код_помещения TEXT,
            срок_аренды INTEGER,
            стоимость_аренды REAL
        )
    ''')
    conn.commit()
    conn.close()

# Добавление новой записи
def add_client(fio, room_code, rent_period, rent_cost):
    conn = sqlite3.connect('arendnayabaza.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Клиент (ФИО, код_помещения, срок_аренды, стоимость_аренды) VALUES (?, ?, ?, ?)', (fio, room_code, rent_period, rent_cost))
    conn.commit()
    conn.close()

# Поиск записей по коду помещения
def search_client_by_room_code(room_code):
    conn = sqlite3.connect('arendnayabaza.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Клиент WHERE код_помещения = ?', (room_code,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Удаление записей по ФИО клиента
def delete_client_by_name(name):
    conn = sqlite3.connect('arendnayabaza.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Клиент WHERE ФИО = ?', (name,))
    conn.commit()
    conn.close()

# Редактирование срока аренды по ФИО клиента
def update_rent_period_by_name(name, new_rent_period):
    conn = sqlite3.connect('arendnayabaza.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Клиент SET срок_аренды = ? WHERE ФИО = ?', (new_rent_period, name))
    conn.commit()
    conn.close()

create_table()

add_client('Иванов Иван Иванович', 'A101', 12, 50000.0)
add_client('Петров Петр Петрович', 'B202', 6, 30000.0)
add_client('Сидоров Сидор Сидорович', 'C303', 8, 40000.0)
add_client('Козлова Елена Григорьевна', 'D404', 10, 45000.0)
add_client('Семенова Анна Ивановна', 'E505', 5, 25000.0)
add_client('Николаев Николай Николаевич', 'F606', 7, 35000.0)
add_client('Кузнецов Кирилл Олегович', 'G707', 9, 42000.0)
add_client('Алексеева Ольга Александровна', 'H808', 11, 48000.0)
add_client('Морозов Максим Михайлович', 'I909', 4, 20000.0)
add_client('Павлова Мария Петровна', 'J1010', 3, 15000.0)

print("Все записи:")
conn = sqlite3.connect('arendnayabaza.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Клиент')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()

print("\nПоиск записи по коду помещения 'A101':")
search_result = search_client_by_room_code('A101')
for result in search_result:
    print(result)

delete_client_by_name('Иванов Иван Иванович')

print("\nВсе записи после удаления:")
conn = sqlite3.connect('arendnayabaza.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Клиент')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()

update_rent_period_by_name('Петров Петр Петрович', 8)