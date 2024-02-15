
from timeit import timeit as timeit_method
from timeit import repeat
from timeit import default_timer
from cProfile import run
import time

#
# """
# Задание 1.
#
# Приведен код, который позволяет сохранить в
# массиве индексы четных элементов другого массива
#
# Сделайте замеры времени выполнения кода с помощью модуля timeit
#
# Попробуйте оптимизировать код, чтобы снизить время выполнения.
# Проведите повторные замеры
#
# ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
# """
#
#
# def func_1(nums):
#     new_arr = []
#     for i in range(len(nums)):
#         if nums[i] % 2 == 0:
#             new_arr.append(i)
#     return new_arr
#
#
# def func_2(nums):
#     return [i for i in range(len(nums)) if not nums[i] % 2]
#
#
# def func_3(nums):
#     new_arr = []
#     new_arr += [i for i in range(len(nums)) if not nums[i] % 2]
#     return new_arr
#
#
# def func_4(nums, arr):
#     list(map(lambda x: arr.append(x), [i for i in range(len(nums)) if i % 2 == 0]))
#     return arr
#
#
# test_code = """
# arr = [i for i in range(len(list(range(10)))) if not list(range(10))[i] % 2]
# """
#
# test_code_2 = """
# new_arr, nums = [], list(range(10))
#
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         new_arr.append(i)
# """
#
# test_code_3 = """
# arr_w = []
# nums, delta = 10, 2
# while delta <= nums:
#     arr_w += [nums - delta]
#     delta += 2
# """
# recursion = """
# def Foo3(arr, num):
#     num -= 2
#     if num < 0:
#         return list(reversed(arr))
#     arr += [num]
#     return Foo3(arr, num)
# """
# times = []
# def time_func(arg_stmt):
#     t1 = timeit_method(arg_stmt, 'pass', default_timer, 100, globals())
#     # rep = repeat(arg_stmt, 'pass', default_timer, 3, 10000, globals=globals())
#     # return f'{arg_stmt}\n{list(map(lambda x: x * 1000, rep))}\n'
#     times.append(f'{arg_stmt}  {t1}')
#
# print(time_func('func_1'))
# print(time_func('func_2'))
# print(time_func('func_3'))
# print(time_func(test_code))
# print(time_func(test_code_2))
# print(time_func(test_code_3))
# print(time_func('func_4'))
# print(time_func(recursion))
#
# for i in sorted(times):
#     print(i)
#     print()
# print(time_func(str(test_code)))
# print(repeat(test_code, 'from __main__ import test_code', default_timer, 3, 10000))

# Код ускорен в func_4 при repeat. Как я понял, функция лямбда очень сильно ускоряет работу, несмотря на то, что мы совершаем
# лишние действия:(добавление в пустой список через лямбду результаты выполнения ls), func_2 имеет только этот самый ls,
# но работает почти в два раза медленнее. Не совсем понятно, почему так, но это факт. При обычном timeit самый быстрый
# код test_code.


#
# """
# Задание 2.
#
# Приведен код, который формирует из введенного числа
# обратное по порядку входящих в него цифр.
# Задача решена через рекурсию
# Выполнена попытка оптимизировать решение мемоизацией
# Сделаны замеры обеих реализаций.
#
# Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
#
# П.С. задание не такое простое, как кажется
# """
#
# from timeit import timeit
# from random import randint
#
#
# def recursive_reverse(number):
#     if number == 0:
#         return str(number % 10)
#     return f'{str(number % 10)}{recursive_reverse(number // 10)}'
#
#
# num_100 = randint(10000, 1000000)
# print(num_100)
# num_1000 = randint(1000000, 10000000)
# num_10000 = randint(100000000, 10000000000000)
#
# print('Не оптимизированная функция recursive_reverse')
# print(
#     timeit(
#         "recursive_reverse(num_100)",
#         setup='from __main__ import recursive_reverse, num_100',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_1000)",
#         setup='from __main__ import recursive_reverse, num_1000',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_10000)",
#         setup='from __main__ import recursive_reverse, num_10000',
#         number=10000))
#
#
# def memoize(f):
#     cache = {}
#
#     def decorate(*args):
#         if args in cache:
#             return cache[args]#эта проверка сделана для того,
#             # чтобы словарь не захлебывался, так как много вызовов в проверке времени
#         else:
#
#             cache[args] = f(*args)
#             return cache[args]
#
#
#     return decorate
#
#
# @memoize
# def recursive_reverse_mem(number):
#     if number == 0:
#         return ''
#     return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'
#
#
# print('Оптимизированная функция recursive_reverse_mem')
# print(
#     timeit(
#         'recursive_reverse_mem(num_100)',
#         setup='from __main__ import recursive_reverse_mem, num_100',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_1000)',
#         setup='from __main__ import recursive_reverse_mem, num_1000',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_10000)',
#         setup='from __main__ import recursive_reverse_mem, num_10000',
#         number=10000))


# """
# Задание 3.
#
# Приведен код, формирующий из введенного числа
# обратное по порядку входящих в него
# цифр и вывести на экран.
#
# Сделайте профилировку каждого алгоритма через timeit
#
# Обязательно предложите еще свой вариант решения!
#
# Сделайте вывод, какая из четырех реализаций эффективнее и почему!
# """
#
from cProfile import run
from timeit import timeit as time_method
def deco(func):
    d = {
    }
    def wrapper(*args):

        if args in d:
            return d[args]
        else:

            d[args] = func(*args)
            return d[args]

    return wrapper

@deco

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


@deco
def revers_4(enter_num):
    return ''.join(list(reversed(' '.join(str(enter_num)).split())))

print(timeit_method('revers_4', 'pass', default_timer, 10))
# def time_Foo(arg_func):
#     print(revers_4('Hellow'))
#     t1 = timeit_method(arg_func, 'from __main__ import reverse_4', default_timer,100)
#     return (t1 * 1000000).__round__(3)
# print(time_Foo('revers_4(1234)'))
# print(time_Foo('revers(1234)'))
# print(time_Foo('revers_2'))
# print(time_Foo('revers_3'))

#4 функция эффективнее так как работает быстрее из-за меньшего количества строк кода и благодаря более просто О-нотации.
#добавив мемоизацию код стал еще быстрее

t = time.perf_counter()

time.sleep(2)
print(time.perf_counter() - t)















# """
# Задание 4.
#
# Приведены два алгоритма. В них определяется число,
# которое встречается в массиве чаще всего.
#
# Сделайте профилировку каждого алгоритма через timeit
#
# Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
# Сделайте замеры и опишите, получилось ли у вас ускорить задачу
# """
#
# array = [2, 3, 2, 3, 5, 4, 4,2,6,1,4,2,6,7,8,1,4,3,6,2,3,6,1,1,1,1]
# print(array.index(6))
#
# def func_1():
#     m = 0
#     num = 0
#     for i in array:
#         count = array.count(i)
#         if count > m:
#             m = count
#             num = i
#     return f'Чаще всего встречается число {num}, ' \
#            f'оно появилось в массиве {m} раз(а)'
#
#
# def func_2():
#     new_array = []
#     for el in array:
#         count2 = array.count(el)
#         new_array.append(count2)
#     max_2 = max(new_array)
#     elem = array[new_array.index(max_2)]
#
#     return f'Чаще всего встречается число {elem}, ' \
#            f'оно появилось в массиве {max_2} раз(а)'
#
# print(func_2())
# def func_3():
#     lam_func = list(map(lambda x: array.count(x), array))
#     return f'Число {array[lam_func.index(max(lam_func))]} встречается {max(lam_func)} раз'
#
# def time_profile(arg_stmt):
#     setup = f'from __main__ import {arg_stmt}'
#     return (timeit_method(arg_stmt, setup, default_timer, 100, globals()) * 1000000).__round__(3)
# print(time_profile('func_1'))
# print(time_profile('func_2'))
# print(time_profile('func_3'))
#
# print()
