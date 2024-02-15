import random
import hashlib
import sqlite3
import string
import time
import webbrowser

# """
# Задание 1.
# Реализуйте функции:
#
# a) заполнение списка, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    заполнение словаря, оцените сложность в O-нотации операции нужно проводить в цикле)
#    сделайте аналитику, что заполняется быстрее и почему
#    сделайте замеры времени
# b) получение элемента списка, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    получение элемента словаря, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    сделайте аналитику, что заполняется быстрее и почему
#    сделайте замеры времени
# с) удаление элемента списка, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    удаление элемента словаря, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    сделайте аналитику, что заполняется быстрее и почему
#    сделайте замеры времени
#
#
# ВНИМАНИЕ: в задании три пункта
# НУЖНО выполнить каждый пункт
# обязательно отделяя каждый пункт друг от друга
#
# Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
# вы уже знаете, что такое декоратор и как его реализовать,
# обязательно реализуйте ф-цию-декоратор и пусть она считает время
# И примените ее к своим функциям!
# """
#
#
# time_list, time_dict = [], []
#
#
# def time_dec(func):
#     def wrapper(*args):
#         start = time.time()
#         var = func(*args)
#         end = time.time()
#         if isinstance(args[0], list):
#             time_list.append((end - start).__round__(10))
#         elif isinstance(args[0], dict):
#             time_dict.append((end - start).__round__(10))
#         print(f'Время работы функции {func.__name__}: {(end - start).__round__(10)} секунд')
#         return var
#
#     return wrapper
#
#
# @time_dec
# def push_lst(arg_lst, num):
#     for i in range(num):
#         element = rnd.randint(1, num)
#         arg_lst.append(element)
#     return arg_lst
# #
# #
# # arr = []
# # n = 1000
# # push_lst(arr, n)
# #
# #
# # @time_dec
# # def push_dct(arg_dct, num):
# #     for i in range(num):
# #         arg_dct.setdefault(i, i)
# #     return arg_dct
# #
# #
# # dictionary = {
# #
# # }
# # push_dct(dictionary, n)
# # print('#' * 100)
# #
# #
# # # -------------------
# # @time_dec
# # def element_list(arg_list):
# #     idx = rnd.randint(1, len(arg_list))
# #     return arg_list[idx]
# #
# #
# # element_list(arr)
# #
# #
# # @time_dec
# # def element_dict(arg_dict):
# #     random_key = rnd.randint(1, len(arg_dict))
# #     return arg_dict.get(random_key)
# #
# #
# # element_dict(dictionary)
# # print('#' * 100)
# #
# #
# # # -------------------
# # @time_dec
# # def oup_list(arg_list):
# #     idx = rnd.randint(1, len(arg_list))
# #     return arg_list.pop(idx)
# #
# #
# # oup_list(arr)
# #
# #
# # @time_dec
# # def out_dict(arg_dict):
# #     random_key = rnd.randint(1, len(arg_dict))
# #     return arg_dict.pop(random_key)
# #
# #
# # out_dict(dictionary)
# #
# # """" ИТОГ! Время работы функций по словарю гораздо быстрее, чем по списку"""
#
# """
# Задание 2.
#
# Ваша программа должна запрашивать пароль
# Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
# Для генерации хеша обязательно нужно использовать криптографическую соль
# Обязательно выведите созданный хеш
#
# Далее программа должна запросить пароль повторно и вновь вычислить хеш
# Вам нужно проверить, совпадает ли пароль с исходным
# Для проверки необходимо сравнить хеши паролей
#
# ПРИМЕР:
# Введите пароль: 123
# В базе данных хранится строка: 555a3581d37993843efd4eba1921
# f1dcaeeafeb855965535d77c55782349444b
# Введите пароль еще раз для проверки: 123
# Вы ввели правильный пароль
#
# Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
# или, если вы уже знаете, как Python взаимодействует с базами данных,
# воспользуйтесь базой данный sqlite, postgres и т.д.
# п.с. статья на Хабре - python db-api
# """
#
#
# # Создадим базу данных при помощи SQlite3.
# class DATABASE:
#     def __init__(self, name_database):
#         self.name_database = name_database
#         self.conn = sqlite3.connect(self.name_database)  # Подключение к БД
#         self.cur = self.conn.cursor()  # Создание курсора (спец. атрибута) для команд SQL
#
#     def create_table(self):  # создание таблицы в текущей БД
#         self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
#                             login_db TEXT PRIMARY KEY,
#                             password_db TEXT);"""
#                          )
#
#     def ins_table(self, insert_commit, *args):  # наполнение таблицы в текущей БД
#         print(f'ДАННЫЕ {args}')
#         try:
#             self.cur.execute("""INSERT INTO users VALUES(?, ?);""", args)  # знаки вопроса для добавления в
#             # строки таблицы кортеж из значений
#         except sqlite3.IntegrityError:  # если такие значения существуют (ловим ошибку)
#             print(f'Такой пользователь уже зарегистрирован!')
#         else:
#             if insert_commit:  # фиксация добавления элемента (окончательное добавление)
#                 print(f'Окончательный занос')
#                 self.conn.commit()
#
#     def clean_table(self, clean_commit, *args):  # очищение таблицы в текущей БД
#         self.cur.execute("""DELETE FROM users WHERE login_db IN (?, ?);""", args) if args \
#             else self.cur.execute("""DELETE FROM users;""")
#
#         if clean_commit:  # фиксация удаления (окончательное удаление)
#             self.conn.commit()
#
#     def view_table(self):
#         self.cur.execute("""SELECT * FROM users;""")
#         return self.cur.fetchall()
#
#
# db_hash = DATABASE("data_users.db")
#
# db_hash.create_table()
#
#
# def clean_db(*args):
#     db_hash.clean_table(1, *args)
#
#
# # Создадим несколько пользователей в базе для большей реалистичности. Будем использовать словарь.
# # Если база пустая - заполняем её фейковыми юзерами
# if not len(db_hash.view_table()):
#     dict_users = {
#     }
#     letters = string.ascii_uppercase
#
#     # Заполнение через рекурсию
#     def push_dict(arg_dict, arg_letters):
#         if len(arg_dict) == 10:
#             return arg_dict
#         name_user = random.choice(arg_letters)
#         new_letters = arg_letters.replace(name_user, '')
#         dict_users.setdefault(name_user * 3, hashlib.sha256(name_user.encode()
#                                                             + str(random.randint(1, 10000)).encode()).hexdigest())
#         return push_dict(arg_dict, new_letters)
#
#
#     push_dict(dict_users, letters)
#     for name, salt_hash in dict_users.items():
#         db_hash.ins_table(True, name, salt_hash)
#
# # Регистрация нового пользователя в базу.
# # По этой ветке мы проверяем, есть ли пользователь в базе.
# # Если да, то ловим исключение и выводим соотв. сообщение (try, except выше в классе). Иначе, заносим юзера в БД.
# ENTER = input('Войти (нажмите E)/Зарегистрироваться (нажмите R)')
# if ENTER == 'R':
#     login = input('Введите ваше имя для регистрации ')
#     while 1:
#         password = input('Введите пароль (не менее 5 символов!) ')
#         if len(password) >= 5:
#             break
#         else:
#             print(f'Слишком короткий пароль! Сделайте длиннее')
#     password_hash = hashlib.sha256(login.encode() + password.encode()).hexdigest()
#     db_hash.ins_table(True, login, password_hash)
# # По этой ветке мы проверяем, совпадают ли введенные данные с данными в базе (которую я возвращаю списком кортежей).
# # Если да, то заходим, если нет, то выводим соотв. сообщение.
# elif ENTER == 'E':
#     # Проверка входа
#     login_enter = input('Введите ваше имя ')
#     password_enter = input('Введите пароль ')
#     password_enter_hash = hashlib.sha256(login_enter.encode() + password_enter.encode()).hexdigest()
#     if (login_enter, password_enter_hash) in db_hash.view_table():
#         print(f'Здравствуйте {login_enter}! Вы вошли!')
#     else:
#         print(f'Неверное имя пользователя и/или пароль!')
# else:
#     ...
# for i in db_hash.view_table():
#     print(i)
###############################################
# """
# Задание 3.
# Определить количество различных (уникальных) подстрок
# с использованием хеш-функции
# Дана строка S длиной N, состоящая только из строчных латинских букв
#
# Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
# Все хеши записываем во множество.
# Оно отсечет дубли.
#
# Экономия на размере хранимых данных (для длинных строк) и
# скорость доступа вместе с уникальностью элементов,
# которые даёт множество, сделают решение коротким и эффективным.
#
# Пример:
# рара - 6 уникальных подстрок
#
# рар
# ра
# ар
# ара
# р
# а
# """
# s2 = 'papa'
# s = 'qwerty'
# low_strings = set()
#
#
# def foo(arg_string):
#     for letter in arg_string:
#         step = arg_string.index(letter)
#         while step <= len(arg_string) - 1:
#             if arg_string[arg_string.index(letter):step + 1] == arg_string:
#                 break
#             else:
#                 low_string = arg_string[arg_string.index(letter):step + 1]
#                 hash_low_string = hashlib.sha256(low_string.encode()).hexdigest()
#                 low_strings.add(hash_low_string)
#             step += 1
#
#
# foo(s2)
# low_strings = set(low_strings)
# for i in low_strings:
#     print(i)
#############################################################
"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""


# url1, url2, url3 = 'https://pythonpip.ru', 'https://www.wildberries.ru', 'https://www.youtube.com'
#
# kash = {
#     url1: hashlib.sha512(url1.encode() + ''.join(reversed(url1)).encode()).hexdigest(),
#     url2: hashlib.sha512(url1.encode() + ''.join(reversed(url2)).encode()).hexdigest(),
#     url3: hashlib.sha512(url1.encode() + ''.join(reversed(url3)).encode()).hexdigest()
# }
# for i in kash.items():
#     print(i)
# def urls(arg_url):
#     print(''.join(reversed(arg_url)))
#     if arg_url in kash:
#         return f'страница есть! её хэш {kash[arg_url]}\n'
#     if not arg_url in kash:
#         url_hash = hashlib.sha512(arg_url.encode() + ''.join(list(reversed(arg_url))).encode()).hexdigest()
#         kash.setdefault(arg_url, url_hash)
#     # if kash[arg_url]:
#     #     return f'страница есть! её хэш {kash[arg_url]}'
#     # elif not kash[arg_url]:
#     #     return 'dasd'
# print(urls('https://pythonpip.ru'))
# for i in kash.items():
#     print(i)

# url1 = 'https://pythonpip.ru'
# class Cash:
#     def __init__(self):
#
#         self.dictionary_url = {
#
#         }
#
#     def update_dict(self, url):
#         self.dictionary_url.setdefault(url, hashlib.sha512(url.encode() + ''.join(reversed(url)).encode()).hexdigest())
#     def urls(self):
#         return self.dictionary_url
#     def view_urls(self, url_key):
#         return f'{url_key}: {self.dictionary_url[url_key]}'
#
# cash = Cash()
# cash.update_dict(url1)
# test_url = 'https://www.wildberries.ru'
# if test_url in cash.urls():
#     print(f'страница есть: {cash.view_urls(test_url)}')
# else:
#     cash.update_dict(test_url)
# print(cash.urls())
# if test_url in cash.view_urls():
#     print(f'страница есть! это{test_url}: {cash.view_urls()[test_url]}')
# РЕШЕНИЕ ЧЕРЕЗ БАЗУ ДАННЫХ
class Db_urls:
    def __init__(self):
        self.conn = sqlite3.connect('urls_hash.db')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
                        CREATE TABLE IF NOT EXISTS urls(
                         site_name TEXT PRIMARY KEY,
                         url_db TEXT,
                         hash_db TEXT);
                         """
                         )

    def insert_table(self, commit, *args):
        try:
            self.cur.execute("""INSERT INTO urls VALUES(?,?,?);""", args)
        except sqlite3.IntegrityError:
            print(f'Такая страница уже есть в БД!')
        else:
            if commit:
                self.conn.commit()

    def clean_table(self, commit, *args):
        if args:
            self.cur.execute("""DELETE FROM urls WHERE site_name IN (?);""", args)
        else:
            self.cur.execute("""DELETE FROM urls;""")
        if commit:
            self.conn.commit()

    def view_table(self):
        self.cur.execute("""SELECT * FROM urls;""")
        return self.cur.fetchall()


db_urls = Db_urls()


def Foo_insert_db(val1, val2):
    hash_site = hashlib.sha512(val1.encode() + val2.encode()).hexdigest()
    print(type(hash_site))
    db_urls.insert_table(1, val1, val2, hash_site)


# Foo_insert_db('GIT', 'https://github.com')
for i in db_urls.view_table():
    print(i)

site = input(f'Введите интересующий сайт: ')

for i in db_urls.view_table():
    print(site)
    print(i)
    if site in i:
        print('ddd')
        if i[0] == site:
            webbrowser.open_new_tab(i[1])
            print(i[1])

    else:
        webbrowser.open_new_tab('https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwjh9o6-uf2AAxUxDRAIHWqwDGIQPAgJ')
        new_url = input('Введите новый URL: ')
        Foo_insert_db(site, new_url)
        break

for i in db_urls.view_table():
    print(i)
