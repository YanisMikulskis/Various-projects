import sqlite3
import string
import hashlib
import random
from memory_profiler import profile, memory_usage
from timeit import default_timer
import numpy

"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

import random


def deco(func):
    def wrapper(*args):
        print()
        print(func.__name__)
        m1, t1 = memory_usage()[0], default_timer()
        res = func(*args)


        m2, t2 = memory_usage()[0], default_timer()

        print(f'память: {m2 - m1}\nвремя\n{t2 - t1}')
        return res

    return wrapper


arr = [random.randint(random.randint(1, 1000), 1000) for i in range(10000)]


@deco
def Alg_1(lst, result):
    for i in lst:
        if not result:
            result.append(i)
        for j in lst[lst.index(i):]:
            result[0] = j if j < result[0] else result[0]
    return result[0]


Alg_1(arr, [])


@deco
def f(lst):
    res = lambda x: sorted(x)[0]
    return res(lst)


print(f(arr))


# Идеальное решение. Занимает минимум памяти, а до 10000 итерация вообще ничего не занимает
@deco
def optima(lst, result):
    for i in lst:
        result[0] = i if result[0] > i else result[0]
    return result


# print(optima(arr, [arr[0]]))
# был полностью переписан код и убран двойной цикл (квадратичная сложность).
# Затраты памяти и времени были существенно уменьшены. Были сделаны два новых варианта.
