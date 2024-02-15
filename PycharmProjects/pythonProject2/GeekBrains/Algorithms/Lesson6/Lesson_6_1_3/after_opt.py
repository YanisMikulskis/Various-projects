# Задание 2.
"""
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import collections
import sqlite3, random, hashlib, string, pprint, json

import numpy
from memory_profiler import memory_usage
from timeit import default_timer


# Создадим базу данных при помощи SQlite3.
def deco(func):
    def wrapper(*args):
        m1, t1 = memory_usage()[0], default_timer()
        res = func(*args)
        m2, t2 = memory_usage()[0], default_timer()
        print(f'Memory {m2 - m1}\nTime {t2 - t1}')
        return res

    return wrapper


@deco
# Memory 0.859375
# Time 1.2851409160066396   (при 100 значениях)

# Memory 2.453125
# Time 2.9486684590083314   (при 1000 знач)

def pre_opt():
    class DATABASE:
        __slots__ = ['name_database', 'conn', 'cur', 'var']

        def __init__(self, name_database):
            self.name_database = name_database
            self.conn = sqlite3.connect(self.name_database)  # Подключение к БД
            self.cur = self.conn.cursor()  # Создание курсора (спец. атрибута) для команд SQL

        def create_table(self):  # создание таблицы в текущей БД
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                                login_db TEXT PRIMARY KEY,
                                password_db TEXT);"""
                             )

        def ins_table(self, insert_commit, *args):  # наполнение таблицы в текущей БД
            try:
                self.cur.execute("""INSERT INTO users VALUES(?, ?);""", args)  # знаки вопроса для добавления в
                # строки таблицы кортеж из значений
            except sqlite3.IntegrityError:  # если такие значения существуют (ловим ошибку)
                print(args[0])

                print(f'Такой пользователь уже зарегистрирован!')
            else:
                if insert_commit:  # фиксация добавления элемента (окончательное добавление)
                    self.conn.commit()

        def clean_table(self, clean_commit, *args):  # очищение таблицы в текущей БД
            self.cur.execute("""DELETE FROM users WHERE login_db IN (?, ?);""", args) if args \
                else self.cur.execute("""DELETE FROM users;""")
            self.conn.commit() if clean_commit else ...  # фиксация удаления (окончательное удаление)

        def view_table(self):
            self.cur.execute("""SELECT * FROM users;""")
            return self.cur.fetchall()

    db_hash = DATABASE("data_users.db")

    db_hash.create_table()
    clean_db = lambda *args: db_hash.clean_table(1, *args)
    clean_db()
    # Создадим несколько пользователей в базе для большей реалистичности. Будем использовать словарь.
    # Если база пустая - заполняем её фейковыми юзерами
    if not len(db_hash.view_table()):
        letters = string.ascii_uppercase
        data_user = lambda name, password: numpy.array([name * random.randint(1, 5),
                                                        hashlib.sha256(name.encode() + password.encode()).hexdigest()])
        all_data = numpy.array([data_user(''.join([random.choice(letters)
                                                   for _ in range(random.randint(1, 10))]),
                                          str(random.randint(1, 10000))) for _ in range(1000)])

        name_users = numpy.array([data[0] for data in all_data])
        all_data = numpy.array([[data[0] + random.choice(letters) * random.randint(1, 20),
                                 data[1]] if numpy.count_nonzero(name_users == data[0]) > 1
                                else data for data in all_data])

        [db_hash.ins_table(True, data[0], data[1]) for data in all_data]
    # Регистрация нового пользователя в базу.
    # По этой ветке мы проверяем, есть ли пользователь в базе.
    # Если да, то ловим исключение и выводим соотв. сообщение (try, except выше в классе). Иначе, заносим юзера в БД.
    ENTER = input('Войти (нажмите E)/Зарегистрироваться (нажмите R)')
    if ENTER == 'R':
        login = input('Введите ваше имя для регистрации ')
        while 1:
            password = input('Введите пароль (не менее 5 символов!) ')
            if len(password) >= 5:
                break
            else:
                print(f'Слишком короткий пароль! Сделайте длиннее')
        password_hash = hashlib.sha256(login.encode() + password.encode()).hexdigest()
        db_hash.ins_table(True, login, password_hash)
    # По этой ветке мы проверяем, совпадают ли введенные данные с данными в базе (которую я возвращаю списком кортежей).
    # Если да, то заходим, если нет, то выводим соотв. сообщение.
    elif ENTER == 'E':
        # Проверка входа
        login_enter = input('Введите ваше имя ')
        password_enter = input('Введите пароль ')
        password_enter_hash = hashlib.sha256(login_enter.encode() + password_enter.encode()).hexdigest()
        print(f'Здравствуйте {login_enter}! Вы вошли!') if \
            (login_enter, password_enter_hash) in \
            db_hash.view_table() else print(f'Неверное имя пользователя и/или пароль!')

    else:
        print(f'Выберите регистрацию или вход!')
for i in range(10):
    pre_opt()

# Уменьшил время, но увеличились затраты памяти.
# Был реализован лгоритм создания пользователей в базу с помощью numpy. Это при больших БДю При маленьких все наоборот
# - меньше памяти, но дольше времени срабатывает. В целом разницы нет, но нумпай более мощный инструмент
