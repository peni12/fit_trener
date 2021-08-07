import sqlite3


def sqlite_add(data, prisi_bool=False, jump_bool=False):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        # sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
        #                             id INTEGER PRIMARY KEY,
        #                             data datetime NOT NULL,
        #                             prisedaniye INTEGER,
        #                             jump INTEGER);'''


        sqlite_insert_query = """INSERT INTO sqlitedb_developers
                                (data, prisedaniye, jump) VALUES (?, 0, 0)"""


        sqlite_select_query = """select * from sqlitedb_developers where data = ?"""


        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        # cursor.execute(sqlite_create_table_query)
        # cursor.execute(sqlite_insert_query)
        cursor.execute(sqlite_select_query, (data,))
        print(1)
        records = cursor.fetchall()
        print(2)
        if records == []:
            cursor.execute(sqlite_insert_query, (data,))
            cursor.execute(sqlite_select_query, (data,))
            records = cursor.fetchall()
        print(records)
        if prisi_bool:
            a = int(records[0][2])
            a += 1
        if jump_bool:
            a = int(records[0][3])
            a += 1
        print(1)
        cursor.execute("""UPDATE sqlitedb_developers SET prisedaniye=? WHERE data = ?""", (a,data,))
        print(2)
        cursor.execute(sqlite_select_query, (data,))
        b = cursor.fetchall()
        print(a)
        print(b)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
