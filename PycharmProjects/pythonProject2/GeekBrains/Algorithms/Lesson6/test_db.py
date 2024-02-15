import os
import sqlite3
import os
from pprint import pprint
import string
import random
from memory_profiler import memory_usage
from timeit import default_timer


# os.chdir('/Users/yanis/PycharmProjects/pythonProject2/GeekBrains/Algorithms/Lesson6')
def deco(func):
    def wrapper(*args):
        m1, t1 = memory_usage()[0], default_timer()
        result = func(*args)
        m2, t2 = memory_usage()[0], default_timer()
        print(f'память {m2 - m1}\nВремя {t2 - t1}')
        return result

    return wrapper


@deco
def mkdb():
    class TEST_DB:
        __slots__ = ['conn', 'cur']

        def __init__(self):
            self.conn = sqlite3.connect('test_test.db')
            self.cur = self.conn.cursor()

        def create_table(self):
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS companies(
            name_company TEXT PRIMARY KEY,
            moneys_db INT(10),
            workers INT(10),
            slogan TEXT);
            """)

        def insert_table(self, commit, *args):

            try:
                self.cur.execute("""INSERT INTO companies VALUES(?,?,?,?);""", args)
            except sqlite3.IntegrityError:
                print(f'такое значение есть в БД')
            else:
                if commit:
                    self.conn.commit()

        def clean_table(self, commit):
            if commit:
                self.cur.execute("""DELETE FROM companies;""")

        def view_table(self):
            self.cur.execute("""SELECT * FROM companies;""")
            return self.cur.fetchall()

    test_db = TEST_DB()

    test_db.clean_table(1)




    for i in range(10000):
        lower, upper = string.ascii_lowercase, string.ascii_uppercase
        word = lambda: ''.join(random.choice(lower) for _ in range(random.randint(3, 7)))

        name_company = f'{random.choice(upper)}{word()}'
        money, workers = random.randint(10, 1000), random.randint(30,50)

        words_slogan = ' '.join([word() for _ in range(random.randint(3,7))])
        slogan = f'{random.choice(upper)}{words_slogan}'
        test_db.insert_table(1, name_company, money, workers, slogan)
    pprint(test_db.view_table())
    print(len(test_db.view_table()))



    # if d:
    #     test_db.clean_table(1)
mkdb()
# mkdb(1)
