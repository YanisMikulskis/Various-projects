import sqlite3
conn = sqlite3.connect("orders.db")
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS users (
                userid INT PRIMARY KEY,
                fname TEXT,
                lname TEXT,
                gender TEXT);"""
            )

cur.execute("""CREATE TABLE IF NOT EXISTS orders (
                orderid INT PRIMARY KEY,
                date TEXT,
                userid TEXT,
                total TEXT);"""
            )


datas = ('ффф', 'ы', 'ккк', 'пывп')
try:
    cur.execute("""INSERT INTO users VALUES(?, ?, ?, ?);""", datas)
except sqlite3.IntegrityError:
    print(f'Такое значение уже есть!')

#    VALUES('00001', 'Alex', 'Smith', 'male');""")

cur.execute("select * from users;")
one_result = cur.fetchall()
print(one_result)