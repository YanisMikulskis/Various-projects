from collections import Counter, defaultdict, OrderedDict, namedtuple, ChainMap, deque
from timeit import timeit as time_method
from timeit import default_timer
import string
from memory_profiler import memory_usage
from memory_profiler import profile


# import re
# arr = [1,2,3,4,5,6,7,3,4,4,5,5,5,5,5,5,1,2,3,4,5]
#
# #1
# #
# arr_1 = {arr.count(i) for i in arr}
# print(arr_1)
# #2
# arr_2 = []
# for i in arr:
#     frequency = arr.count(i)
#     if frequency not in arr_2:
#         arr_2.append(frequency)
# print(sorted(arr_2))
#
# #3
# def Foo(lst, freq_lst, idx):
#     if idx > len(lst) - 1:
#         return f'рекурсия {sorted(freq_lst)}'
#     element_now = lst.count(lst[idx])
#     freq_lst.append(element_now) if element_now not in freq_lst else ...
#     idx += 1
#     return Foo(lst, freq_lst, idx)
# print(Foo(arr, [], 0))
# #4
# obj = Counter(arr)
# print(type(obj))
# print(obj)
#
#
# obj_2 = Counter(python=10, java=11)
# print(obj_2)
# obj_elements = list(obj_2.elements())
# obj_freq = [obj_elements.count(i) for i in obj_elements]
# result_set = sorted(list(set([i for i in zip(obj_elements, obj_freq)])))
#
# strings = re.findall(r'\d+', open('numbers.txt', 'r+').read())
# strings_new = ''.join(strings)
# print(strings_new)
# var2 = Counter(strings_new).most_common()
# print(var2)
# def TF(nums):
#     return {i[0]: (i[1] / len(nums)).__round__(5) for i in var2}
# print(TF(strings_new))
#
# # VAR = list(map(lambda x:Counter(x).most_common(), [''.join(strings)]))
# # VAR_2 = Counter(strings_new).most_common()
# # print(*VAR)
# #
# # print(VAR_2)
#
# print(list(obj_2.most_common()))
# print('\n')
# d = {
#
# }
# d['раз'] = 1
# d['два'] = 2
#
# try:
#     print(d['три'])
# except KeyError:
#     print('ключа нет')
#
# d = defaultdict(list)


# [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 't'], ['y', 'u']]
# def deco(func):
#     def wrapper(*args):
#         m1 = memory_usage()
#         t1 = default_timer()
#         print(t1)
#         result = func(*args)
#         m2 = memory_usage()
#         t2 = default_timer()
#         time_diff = (t2 - t1).__round__(5)
#         mem_diff = m2[0] - m1[0]
#         print(f'функция заняла {mem_diff} памяти\n{time_diff} времени')
#         return result
#     return wrapper
#
# @deco
# def foo(lst):
#     arr_11 = []
#     for i in range(len(lst)):
#         if i != len(lst) - 1 and i % 2 == 0:
#             arr_11.append([lst[i], lst[i+1]])
#     return arr_11
# print(foo(list(range(10000))))


# print(arr_11)
# lst_new = lambda: [arr_10[0], arr_10[1]]
# print(lst_new)
# arr_10 = list(map(lambda x: [arr_10[arr_10.index(x)], arr_10[arr_10.index(x) + 1]] if arr_10.index(x) == 0 else x, arr_10))

# arr_10[0] = [arr_10[0],arr_10[1]]
#
# print(arr_10)
# print(arr_10[0])
#
# print(list([arr_10[0], arr_10[1]]))
# def req(lst, step):
#     print(lst)
#     if step >= len(lst):
#         return lst
#     lst[step] = [lst[step], lst[step + 1]]
#     lst.pop(step + 1)
#     step += 1
#     return req(lst, step)
# print(req(arr_10, 0))
# print(arr_11)
# arr = [('раз', 1), ('два', 2), ('раз', 1), ('два', 2)]
# d1 = defaultdict(list)
# d2 = {}

# s = [('раз', 1), ('два', 2), ('раз', 3), ('два', 4), ('три', 1)]
# d_1 = defaultdict(list)
# d_2 = {}
#
# def check_1():
#     for k, v in s:
#         d_1[k].append(v)
#     return d_1
#
# def check_2():
#     for k, v in s:
#         d_2.setdefault(k, []).append(v)
#
# t1 = time_method('check_1', 'from __main__ import check_1', default_timer, 10, globals()) * 1000000
# t2 = time_method('check_2', 'from __main__ import check_2', default_timer, 10, globals()) * 1000000
# print(t1)
# print(t2)

# SENTENCE = "Ехал Грека через реку, Видит Грека — в реке рак " \
#            "Сунул Грека руку в реку — рак не цапает никак!"
# words = SENTENCE.split()
# print(words)
# word_dict = {
#
# }
#
# word_defdict = defaultdict(int)
# for i in words:
#     if i in word_dict:
#         word_dict[i] += 1
#     else:
#         word_dict[i] = 1
# print(word_dict)
#
#
#
# print(word_dict)
#
#
# ww = {i:words.count(i) for i in words}
# for i in words:
#     word_defdict[i] += 1
#
# print(word_defdict)
# lets = string.ascii_lowercase
# numbers = [i for i in range(11)]
#
# test_dict_1 = {k:v for k,v in zip(lets[:10], numbers)}
# test_dict_2 = OrderedDict(test_dict_1)
#
# print(test_dict_1)
# print(test_dict_2)
# var1 = """
# for i in test_dict_1.items():
#     print(i)
# """
#
# var2 = """
# for j in test_dict_2.items():
#     print(j)
# """
# print(time_method('var1', 'pass', default_timer, 10, globals()) * 1000000)
# print(time_method('var2', 'pass', default_timer, 10, globals()) * 1000000)
# RES = namedtuple('resume', 'id fname sname')
# RES_tuple = RES(id=1,
#                 fname='Viktoria',
#                 sname='Brusnikina')
# print(RES)
# print(RES_tuple.fname)
#
# RES_dict = {
#     'id': 1,
#     'fname':'Viktoria',
#     'sname':'Brusnikina'
# }
# print(RES_dict.get('fname'))

# dict_1 = {
#     'One': 1,
#     'Two': 2,
#     'Three': 3
# }
# dict_2 = {
#     'Four': 4,
#     'Two': 2222,
#     'Five': 5
# }
# dict_3 = {
#     'Five':5,
#     'One': 111,
#     'Three': 1000
# }
# all_dicts = ChainMap(dict_1, dict_2, dict_3)
# print(all_dicts['Three'])

# arr = ['1', '2', 'er', '4']
# for i in arr:
#     if i.isalpha():
#         arr[arr.index(i)] = i.replace(i, '1111')
# print(arr)
# import time
# from timeit import timeit as time_method
# from timeit import default_timer
#
# print(time.time())
# start = time.time()
#
#
# def Foo():
#     arr = []
#     for i in range(100):
#         arr.append(i)
#     print(arr)
#
#
# Foo()
#
# end = time.time()
#
# print(((end - start)))
# print((time_method('Foo', 'pass', default_timer, 1, globals())))
# from collections import namedtuple
# Companies = namedtuple('Companies', 'qua_1 qua_2 qua_3 qua_4')
# C = Companies(
#     qua_1=100,
#     qua_2=123,
#     qua_3=41,
#     qua_4=000
# )
# print(C)
# print(Companies)
# import string
# from itertools import zip_longest
# arr = [num for num in range(11)]
# letters = [let for let in string.ascii_lowercase]
#
# new_arr = zip(arr, letters)
# new_arr2 = zip_longest(arr, letters)
# print(list(new_arr))
# print(list(new_arr2))
# from functools import reduce
# arr = [4,5,6]
# def Foo(x, y):
#     return x + y
# # print(reduce(Foo, arr, 0))

# numbers = [str(i) for i in range(6)]
# i = 'C'
# letters = namedtuple('letters', 'A B C D E F')(*numbers)
# print(n(letters))
# print(i.__repr__())
# print(letters.A)
#
# arr1 = ['1', 'b', '4', '5']
# arr2 = ['a', 'b', 'c', 'd']
# print(list(set(arr1) & set(arr2)))
#
# def foo(lst, idx):
#     if idx > len(lst) - 1:
#         return sum(lst)
#     print(idx)
#     print(f'{16 ** idx} dfdfdd')
#     lst[idx] = lst[idx] * (16 ** idx)
#     idx += 1
#     return foo(lst, idx)
# print(foo([8, 10, 3], 0))

# class A:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @staticmethod
#     def static(param):
#
#         return param ** 3
#
#     def m(self):
#         return self.x ** 3 #1000
#
#
#     def met2(self):
#         return A.static(self.x) * 2
#
#     def __add__(self, other):
#
#         print(self.x ** self.y)
#     #
#     # def __sub__(self, other):
#     #     return f'ВИКА БРУСНИЧКА'
#     #
#     # def __mul__(self, other):
#     #     return f'ЭТО УМНОЖЕНИЕ'
#     #
#     # def __truediv__(self, other):
#     #     return f'ЭТО ДЕЛЕНИЕ'
# #
# #
# a = A(10, 20)
# a + 1
#

# def dec(func):
#     def wrapper(*args):
#         return func(*args) * 2
#
#     return wrapper
#
#
# @dec
# def Foo(arg):
#     return arg ** 2
#
#
# print(Foo(10))
# numbers = [num for num in range(10, 16)]
# letters = namedtuple('letters', 'A B C D E F')(*numbers)
#
#
# def decryption(num_16):
#     num_new = list(map(lambda x: int(x) if x.isdigit() else letters._asdict()[x], num_16))
#     def Foo(lst, idx):
#         if idx == len(lst):
#             return lst
#         lst[idx] = lst[idx] * (16 ** idx)
#         idx += 1
#         return Foo(lst, idx)
#
#     result = Foo(num_new, 0)
#     print(result)
#     return sum(result)
#
#
# # @dec
#
# # Переведем число 100010 в шестнадцатеричную систему:
# #
# # 1000 / 16 = 62 (остаток 8)
# # 62 / 16 = 3 (остаток 14, в шестнадцатеричной системе – E)
# # 3 / 16 = 0 (остаток 3)
# # Записываем остатки в обратном порядке, получаем результат: 3E816
# def sum_cryption(num_10, lst):
#     if not num_10:
#         lst.reverse()
#         return lst
#     remainder = num_10 % 16
#     if remainder in letters:
#         remainder = ''.join([name for name, value in letters._asdict().items() if remainder == value])
#     lst.append(remainder)
#     num_10 = num_10 // 16
#     return sum_cryption(num_10, lst)
#
#
#
# print(sum_cryption(1000, []))
#
# ar= 1
# ar *= 5
# ar *= 10
# print(ar)
# print(5 * 10)
# num_1 = '3E8'
# arr_1 = [_ for _ in reversed(num_1)]
#
# num_2 = '5A'
# arr_2 = [_ for _ in reversed(num_2)]
# print(decryption(arr_1) + decryption(arr_2))
# # foo(decryption(arr_1))
# print(3//16)
#
# def all_remove(iterable, el):
#     [dq_copy.remove(el) for _ in range(iterable.count(el))]
#
# dq = deque('Hello')
# dq_copy = dq.copy()
# print(dq_copy)
# for _ in range(dq_copy.count('l')):
#     dq_copy.remove('l')
# func = lambda x: [dq_copy.remove(x) for _ in range(dq_copy.count(x))]
# func('l')
# print(dq_copy)
# dq2 = []
# dq2.pop()
# arr = [1,2,3,45,4]
# arr.pop(0)
# # qwe = 'HELLO'
# # qwe_l = ' '.join(qwe).split()
# # var = ' '.join('FLAG').split()
# # while n != len(var):
# #     dq.insert(n, var[n])
# #     n += 1
#
#
# print(dq)
#
#
#
# def Fo
# from pyheat import PyHeat
# ph = PyHeat('Lesson 5.3.py')
# ph.create_heatmap()
# # To view the heatmap.
# ph.show_heatmap()
# # To output the heatmap as a file.
# ph.show_heatmap('image_file.png')
# from cProfile import run
# def foo():
#     return [i for i in range(1000)]
# print(run('foo()'))


def deco(func):
    def wrapper(*args):
        m1 = memory_usage()
        t1 = default_timer()
        result = func(*args)
        m2 = memory_usage()
        t2 = default_timer()
        time_diff = (t2 - t1).__round__(5)
        mem_diff = (m2[0] - m1[0]).__round__(2)

        print(f'функция {func.__name__} заняла {mem_diff} памяти\n{time_diff} времени')
        return result

    return wrapper


# @profile
@deco
def foo(lst):
    arr_11 = []
    for i in range(len(lst)):
        if i != len(lst) - 1 and i % 2 == 0:
            arr_11.append([lst[i], lst[i+1]])
    return arr_11
foo(list(range(100000)))

# @profile
# @deco
# def foo_2():
#     class Number:
#         __slots__ = ['numbers', 'arr']
#
#         def __init__(self, numbers, arr):
#             self.numbers = list(range(numbers))
#             self.arr = arr
#
#         def func_job(self):
#             for i in self.numbers:
#                 if i != len(self.numbers) - 1 and not i % 2:
#                     self.arr.append([self.numbers[i], self.numbers[i + 1]])
#             return self.arr
#
#     obj = Number(100000, [])
#     return obj.func_job()


# foo_2()
