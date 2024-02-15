""" Задание 2 из 2 урока"""
import random

from memory_profiler import memory_usage
from timeit import default_timer

"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def deco(f):
    def wrapper(*args):
        m1, t1 = memory_usage()[0], default_timer()

        res = f(*args)
        m2, t2 = memory_usage()[0], default_timer()
        mem_diff, time_diff = m2 - m1, t2 - t1
        print(f'memory: {mem_diff}\ntime {time_diff}')
        return res

    return wrapper


@deco
def main_1():
    number = 532523578931285

    def EVEN(num, rem, even, not_even):
        if not num:
            return f'Количество четных и нечетных цифр в числе равно: ' \
                   f'{len(even), len(not_even)}\n'
        if rem is not None:
            even.append(rem) if rem % 2 == 0 else not_even.append(rem)
            if num < 10:
                even.append(num) if num % 2 == 0 else not_even.append(num)
        return EVEN(num // 10, num % 10, even, not_even)

    print(EVEN(number, None, [], []))


main_1()

print()

t = []


@deco
def main_2():
    number = 532523578931285

    def req(arg_number, even, no_even):
        if not arg_number:
            return f'Количество четных и нечетных цифр в числе равно: {(even, no_even)}'
        now_number, rem = arg_number // 10, arg_number % 10
        if rem % 2 == 0:
            even += 1
        else:
            no_even += 1
        return req(now_number, even, no_even)
    print(req(number, 0, 0))


main_2()
#сократил некоторые вещи те самым уменьшив время