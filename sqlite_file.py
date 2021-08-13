import sqlite3

# sqlite_con = sqlite3.connect('sqlite_python.db')
# cur = sqlite_con.cursor()
# cur.execute("""CREATE TABLE wremya_uprajneniy(
#                     id INTEGER PRIMARY KEY,
#                     total_time INTEGER DEFAULT 0,
#                     time_1 INTEGER DEFAULT 0,
#                     time_2 INTEGER DEFAULT 0,
#                     time_3 INTEGER DEFAULT 0,
#                     upr_4 INTEGER DEFAULT 0,
#                     upr_5 INTEGER DEFAULT 0,
#                     upr_6 INTEGER DEFAULT 0,
#                     upr_7 INTEGER DEFAULT 0,
#                     upr_8 INTEGER DEFAULT 0,
#                     upr_9 INTEGER DEFAULT 0,
#                     upr_10 INTEGER DEFAULT 0,
#                     upr_11 INTEGER DEFAULT 0,
#                     upr_12 INTEGER DEFAULT 0,
#                     upr_13 INTEGER DEFAULT 0,
#                     upr_14 INTEGER DEFAULT 0,
#                     upr_15 INTEGER DEFAULT 0,
#                     upr_16 INTEGER DEFAULT 0);""")
# sqlite_con.commit()
# cur.close()
# sqlite_con.close()





# sqlite_con = sqlite3.connect('sqlite_python.db')
# cur = sqlite_con.cursor()
# cur.execute("""SELECT * FROM statistika_uprajneniye""")
# record = cur.fetchall()
# print(record[0])
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

def statistika_zanyatiy_plus(urj_1=False,urj_2=False,urj_3=False,urj_4=False,urj_5=False,urj_6=False,urj_7=False,
                               urj_8=False,urj_9=False,urj_10=False,urj_11=False,urj_12=False,urj_13=False,urj_14=False,
                               urj_15=False,urj_16=False):
    try:
        sqlite_con = sqlite3.connect('sqlite_python.db')
        cur = sqlite_con.cursor()
        cur.execute("""SELECT * FROM statistika_uprajneniye""")
        record = cur.fetchall()
        print(record[0])
        a = record[0]
        c = int(a[1])
        c += 1
        cur.execute("""UPDATE statistika_uprajneniye SET total_reps=?""", (c,))
        if urj_1:
            b = int(a[2])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_1=?""", (b,))
        elif urj_2:
            b = int(a[3])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_2=?""", (b,))
        elif urj_3:
            b = int(a[4])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_3=?""", (b,))
        elif urj_4:
            b = int(a[5])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_4=?""", (b,))
        elif urj_5:
            b = int(a[6])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_5=?""", (b,))
        elif urj_6:
            b = int(a[7])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_6=?""", (b,))
        elif urj_7:
            b = int(a[8])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_7=?""", (b,))
        elif urj_8:
            b = int(a[9])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_8=?""", (b,))
        elif urj_9:
            b = int(a[10])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_9=?""", (b,))
        elif urj_10:
            b = int(a[11])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_10=?""", (b,))
        elif urj_11:
            b = int(a[12])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_11=?""", (b,))
        elif urj_12:
            b = int(a[13])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_12=?""", (b,))
        elif urj_13:
            b = int(a[14])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_13=?""", (b,))
        elif urj_14:
            b = int(a[15])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_14=?""", (b,))
        elif urj_15:
            b = int(a[16])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_15=?""", (b,))
        elif urj_16:
            b = int(a[17])
            b += 1
            cur.execute("""UPDATE statistika_uprajneniye SET upr_16=?""", (b,))

        sqlite_con.commit()
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_con):
            sqlite_con.close()
            print("Соединение с SQLite закрыто")
def statistika_posle_zanyatiy(urj_1=False,urj_2=False,urj_3=False,urj_4=False,urj_5=False,urj_6=False,urj_7=False,
                               urj_8=False,urj_9=False,urj_10=False,urj_11=False,urj_12=False,urj_13=False,urj_14=False,
                               urj_15=False,urj_16=False):
    try:
        sqlite_con =sqlite3.connect('sqlite_python.db')
        cur = sqlite_con.cursor()

        cur.execute("""SELECT * FROM statistika_uprajneniye""")
        record = cur.fetchall()
        print(record[0])
        a = record[0]
        b = []
        b.append(str(a[1]))
        if urj_1:
            b.append(str(a[2]))
            return b
        elif urj_2:
            b.append(str(a[3]))
            return b
        elif urj_3:
            b.append(str(a[4]))
            return b
        elif urj_4:
            b.append(str(a[5]))
            return b
        elif urj_5:
            b.append(str(a[6]))
            return b
        elif urj_6:
            b.append(str(a[7]))
            return b
        elif urj_7:
            b.append(str(a[8]))
            return b
        elif urj_8:
            b.append(str(a[9]))
            return b
        elif urj_9:
            b.append(str(a[10]))
            return b
        elif urj_10:
            b.append(str(a[11]))
            return b
        elif urj_11:
            b.append(str(a[12]))
            return b
        elif urj_12:
            b.append(str(a[13]))
            return b
        elif urj_13:
            b.append(str(a[14]))
            return b
        elif urj_14:
            b.append(str(a[15]))
            return b
        elif urj_15:
            b.append(str(a[16]))
            return b
        elif urj_16:
            b.append(str(a[17]))
            return b

        sqlite_con.commit()
        cur.close()
        return b

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_con):
            sqlite_con.close()
            print("Соединение с SQLite закрыто")


def obnuleniye_statistiki_uprajneniy():
    try:
        sqlite_con = sqlite3.connect('sqlite_python.db')
        cur = sqlite_con.cursor()
        for i in range(1, 17):
            cur.execute(f"""UPDATE statistika_uprajneniye SET upr_{i}=0""")
        cur.execute("""UPDATE statistika_uprajneniye SET total_reps=0""")
        sqlite_con.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_con):
            sqlite_con.close()
            print("Соединение с SQLite закрыто")

def wremya_plus(time_1=False, time_2=False, time_3=False):
    try:
        sqlite_con = sqlite3.connect('sqlite_python.db')
        cur = sqlite_con.cursor()

        cur.execute("""SELECT * FROM wremya_uprajneniy""")
        record = cur.fetchall()
        print(record[0])
        a = record[0]

        if time_1:
            b = int(a[2])
            b += 1
            cur.execute("""UPDATE wremya_uprajneniy SET time_1=?""", (b,))
            c = int(a[1])
            c += 1
            cur.execute("""UPDATE wremya_uprajneniy SET total_time=?""", (c,))
        elif time_2:
            b = int(a[3])
            b += 1
            cur.execute("""UPDATE wremya_uprajneniy SET time_2=?""", (b,))
            c = int(a[1])
            c += 1
            cur.execute("""UPDATE wremya_uprajneniy SET total_time=?""", (c,))
        elif time_3:
            b = int(a[4])
            b += 1
            cur.execute("""UPDATE wremya_uprajneniy SET time_3=?""", (b,))
            c = int(a[1])
            c += 1
            cur.execute("""UPDATE wremya_uprajneniy SET total_time=?""", (c,))
        sqlite_con.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_con):
            sqlite_con.close()
            print("Соединение с SQLite закрыто")
def return_time(time_1=False, time_2=False, time_3=False):
    try:
        sqlite_con = sqlite3.connect('sqlite_python.db')
        cur = sqlite_con.cursor()
        cur.execute("""SELECT * FROM wremya_uprajneniy""")
        record = cur.fetchall()
        print(record[0])
        a = record[0]
        b = []
        b.append(str(a[1]))
        if time_1:
            b.append(str(a[2]))
            return b
        elif time_2:
            b.append(str(a[3]))
            return b
        elif time_3:
            b.append(str(a[4]))
            return b
        sqlite_con.commit()
        cur.close()
        return str(a[1])


    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_con):
            sqlite_con.close()
            print("Соединение с SQLite закрыто")

def obnuleniye_wremeni():
    try:
        sqlite_con = sqlite3.connect('sqlite_python.db')
        cur = sqlite_con.cursor()
        for i in range(1, 4):
            cur.execute(f"""UPDATE wremya_uprajneniy SET time_{i}=0""")
        cur.execute("""UPDATE wremya_uprajneniy SET total_time=0""")
        sqlite_con.commit()
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_con):
            sqlite_con.close()
            print("Соединение с SQLite закрыто")