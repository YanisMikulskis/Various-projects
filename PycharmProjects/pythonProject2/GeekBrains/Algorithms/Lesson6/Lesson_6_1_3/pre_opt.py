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
import sqlite3, random, hashlib, string, sys, pprint
from memory_profiler import memory_usage
from timeit import default_timer
# Создадим базу данных при помощи SQlite3.
def deco(func):
    def wrapper(*args):
        m1, t1 = memory_usage()[0], default_timer()
        res = func(*args)
        m2, t2 = memory_usage()[0], default_timer()
        print(f'Memory {m2-m1}\nTime {t2 - t1}')
        return res
    return wrapper
@deco
# Memory 0.84375
# Time 1.3851707089925185   при 100 значениях

# Memory 1.59375
# Time 2.1964283749985043   при 1000 знач

def pre_opt():
    class DATABASE:
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
                print(f'Такой пользователь уже зарегистрирован!')
            else:
                if insert_commit:  # фиксация добавления элемента (окончательное добавление)
                    self.conn.commit()

        def clean_table(self, clean_commit, *args):  # очищение таблицы в текущей БД
            self.cur.execute("""DELETE FROM users WHERE login_db IN (?, ?);""", args) if args \
                else self.cur.execute("""DELETE FROM users;""")

            if clean_commit:  # фиксация удаления (окончательное удаление)
                self.conn.commit()

        def view_table(self):
            self.cur.execute("""SELECT * FROM users;""")
            return self.cur.fetchall()


    db_hash = DATABASE("data_users_pre.db")

    db_hash.create_table()


    def clean_db(*args):
        db_hash.clean_table(1, *args)

    clean_db()
    # Создадим несколько пользователей в базе для большей реалистичности. Будем использовать словарь.
    # Если база пустая - заполняем её фейковыми юзерами
    if not len(db_hash.view_table()):
        dict_users = {
        }
        letters = string.ascii_uppercase
        sys.setrecursionlimit(1200)
        # Заполнение через рекурсию
        def push_dict(arg_dict, arg_letters):
            factor = random.randint(1,5)
            if len(arg_dict) == 1000:
                return arg_dict
            name_user = ''.join([random.choice(arg_letters) for _ in range(random.randint(1,10))])
            # new_letters = arg_letters.replace(name_user, '')
            dict_users.setdefault(name_user * factor, hashlib.sha256(name_user.encode()
                                                                + str(random.randint(1, 10000)).encode()).hexdigest())
            return push_dict(arg_dict, arg_letters)


        push_dict(dict_users, letters)
        for name, salt_hash in dict_users.items():
            db_hash.ins_table(True, name, salt_hash)

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
        if (login_enter, password_enter_hash) in db_hash.view_table():
            print(f'Здравствуйте {login_enter}! Вы вошли!')
        else:
            print(f'Неверное имя пользователя и/или пароль!')
    else:
        print(f'Выберите регистрацию или вход!')
    pprint.pprint(db_hash.view_table())
pre_opt()
