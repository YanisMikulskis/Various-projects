# from sys import getrefcount
# import gc
import os
from memory_profiler import memory_usage
from sys import getsizeof
from pympler import asizeof as AS
import collections as COL
from json import dumps, loads

# arr = list(range(10000))
#
# print(getsizeof(arr))
# print(AS.asizeof(arr))
# class A:
#     def __init__(self):
#         pass
#
# print(getsizeof(A()))
# # class VIKA:
# #     def __init__(self):
# #         ...
# # vika = VIKA()
# # print(getrefcount(vika) - 1)
# # if isinstance(getrefcount(vika), int):
# #     print(True)
#
# # def foo():
# #     arr = [1, 2, 3]
# #     arr.append(arr)
# #     print(id(arr))
# #     print(id(arr[3]))
#
#     return arr
# print(foo())
# obj = gc.collect()
# print(foo())

# class RUSSIA:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#         self.lst = [i for i in range(1000)]
#     def __del__(self):
#         name = self.__class__.__name__
#         print(f'{name} уничтожена')
#
# rus = RUSSIA()
# del rus
# arr = [1,2,3]
# arr.append(arr)
# print(arr)
#
# v = [0,0,0]
# v.append(v)
# print(v)
# obj = gc.collect()
# print(obj)
import memory_profiler
import psutil
from memory_profiler import profile

import random
import time
# arr = [1,2,3]
# arr.append(arr)
# for i in arr:
#     if isinstance(i, list):
#         for it in i:
#             print(it)


# def deco(func):
#     def wrapper(*args, **kwargs):
#         mem_1 = memory_usage()
#         func(args[0])
#
#         mem_2 = memory_usage()
#         mem_inc = mem_2[0] - mem_1[0]
#
#         return f'в функции {func.__name__} и {len(*args)} значениях было использовано {mem_inc} памяти\n'
#     return wrapper
# #
# @deco
# def foo(numbers):
#     for num in numbers:
#         if not num % 2 == 0:
#             yield num
#
#
# @deco
# def foo_2(numbers):
#     return [num for num in numbers if num % 2 == 0]
#
# match __name__:
#     case '__main__':
#         print(foo(list(range(1000))))
#         print(foo_2(list(range(100000))))
#
#
#
# """
# было использовано 38.234375 памяти
# было использовано 0.140625 памяти
# было использовано 0.171875 памяти
# """


# m1 = memory_usage()
# var = 0
# while 1:
#     def foo():
#         return [bin(random.randint(1, 100)) for _ in range(100)]
#     var += 1
#     foo()
#     if var == 1000:
#         break
# m2 = memory_usage()
# print(f'было {m1} MiB\n'
#        f'стало {m2}')

# class A:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# a = A(10,20)
# print(a.__dict__)
# class B:
#     __slots__ = ['x', 'y']
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# print(AS.asizeof(A(10,20)))
# print(AS.asizeof(B(10,20)))
#
# print(getsizeof(A(10,20)))
# print(getsizeof(B(10,20)))

import numpy as nmp
import random as rnd


# arr = [rnd.randint(-100, 100) for i in range(50000)]
# print(AS.asizeof(arr))
# arr_2 = nmp.array([rnd.randint(-100, 100) for j in range(50000)])
# print(AS.asizeof(arr_2))
# print(type(arr_2))
#
# d = {str(num): num for num in range(10)}
# d_tuple = tuple(_ for _ in range(10))
#
# print(getsizeof(d))
# print(getsizeof(d_tuple))
# from recordclass import recordclass as RECORD
# n = COL.namedtuple('name', 'x,y,z')
# ne = n(x=10,
#        y=20,
#        z=30)
# print(ne)
# r = RECORD('name2', 'x,y,z')
# re = r(x=24,
#        y=32,
#        z=100)
#
# de = {'x':24, 'y':32, 'z':100}
# print(getsizeof(ne))
# print(getsizeof(re))
# print(getsizeof(de))
# print(re)
# print(type(r))
# print(type(re))
# re.x = 100000
# print(re)
#
#
# print(ne.x)


# def deco(func):
#     def wrapper(*args, **kwargs):
#         t1 = memory_usage()
#         func(*args)
#         t2 = memory_usage()
#         mem_diff = t2[0] - t1[0]
#         return f'функция {func.__name__} занимает {mem_diff} MiB'
#     return wrapper
#
#
# @deco
# def foo_1(lst):
#     arr = [str(i) for i in lst]
#     return arr
#
#
# print(foo_1(list(range(10000))))
#
#
# @deco
# def foo_2(lst):
#     arr = list(map(lambda x: str(x), lst))
#     print(arr)
#     return arr

#
# gen_dict = {i: i ** 2 for i in range(1001)}
#
# a = None
# gen = dumps(gen_dict)
# print(gen_dict)
#
# ae = {'a':100, 'b':1000}
# with open('numbers.json', 'w+', encoding='utf-8') as file:
#     # file.write(dumps('hello'))
#     file.write(dumps(ae))
#     file.write('\n')
#     file.write(dumps(ae))
#     # for k, v in gen_dict.items():
#     #     s.setdefault(k,v)
#     #
#     #     if k % 10 == 0:
#     #         sd = dumps(s)
#     #         print(sd)
#     #         print(k)
#     #         file.write(sd)
#     #         file.write('\n')
#     #         s = {
#     #
#     #         }
def deco(f):
    def wrapper(*args):
        m1 = memory_usage()
        fet = f(*args)
        print(args)
        m2 = memory_usage()
        res = m2[0] - m1[0]
        print(res)
        return fet
    return wrapper

@deco
def foo(lst):
    arr = [i for i in lst if i % 2 == 0]
    return arr
foo(list(range(10000)))


@deco
def foo_2(lst):
    arr = list(filter(lambda x: x%2 == 0, lst))
    return arr
foo_2(list(range(10000)))