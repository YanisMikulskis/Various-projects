from memory_profiler import memory_usage
from timeit import default_timer
import sys
""" Задание 4 """
"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтись без создания массива!
"""
# print(1 + (-0.5) + 0.25 + (-0.125))
# at = []
# start = 1
# at2 = []
# n = 4
# for i in range(10):
#     at.append(start)
#     start = -start / 2
# print(at)
# n = 4

#
# print(foo(n, 1, 0))
# def deco_2(func):
#     def wrapper(*args):
#         print(func.__name__)
#     return wrapper()

sys.setrecursionlimit(11000)
def deco(func):
    def wrapper(*args):
        m1,t1 = memory_usage()[0], default_timer()
        result = func(*args)
        m2,t2 = memory_usage()[0], default_timer()
        print(f'время {t2 - t1}\nпамять {m2 - m1}\n{func.__name__} - имя функции')
        return result
    return wrapper

def deco_2(func):
    def wrapper(*args):
        print(f'flag {func.__name__}')
    return wrapper

@deco
def wrap():
    n = 10000
    def foo(n, result, arr):
        if not n:
            print(arr)
            print(sum(arr))
            return sum(arr)
        arr.append(result)
        result = -result/ 2
        n -= 1
        return foo(n, result, arr)
    print(foo(n, 1, []))
wrap()


# @deco
# def foo_2(n, var):
#     result = 2 ** (-n) * (-1) if n % 2 != 0 else 2 ** (-n)
#     var += result
#     if not n:
#         return var
#     n -= 1
#     return foo_2(n, var)
#
#
# print(foo_2(n-1, 0))
print()
@deco
def foo_3():
    n2, arr = 4, []
    for number in range(n2):
        arr.append(1/2 ** number)
    arr = list(map(lambda x: x * (-1) if arr.index(x) % 2 != 0 else x, arr))
    return sum(arr)
print(foo_3())
#способ ниже чисто по фану лучше так не делать на практике
n2 = 10000
print(sum(list(map(lambda x: x * (-1) if [(1/2 ** number) for number in range(n2)].index(x) % 2 != 0 else x, [(1/2 ** number) for number in range(n2)]))))

#Превратив рекурсию в цикл, мы уменьшили затраты по памяти достаточно существенно.
# Помимо этого, мы уменьшили время. Данный метод может быть эффективен при небольшом количестве итераций.
# Если требуется, например, просканировать много папок, который находятся друг в друге, то лучше использовать рекурсию.





# #решение через рекурсию первым способом
# n = 5
# def ADD(item):
#     result = 1/2**item if item%2==0 else -1/2**item
#     if item == 0:
#         return result
#     return result + ADD(item - 1)
# print(ADD(n-1)) #вычитаем единичку, так как у нас рекурсия приходит к нулевой степени (item = 0)
# # и дает единицу в i, которая участвует в сумме (см задание)
# #решение через рекурсию вторым способом
# def ADD(item, result):
#     result = abs(result)/2 if item%2==0 else abs(result)/-2
#     if item == 0:
#         return result
#     return result + ADD(item - 1, result)
# print(ADD(n-1, 2))

