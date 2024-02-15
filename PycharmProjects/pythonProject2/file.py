# arr = [-5, 1, 2, 3, 4.7]
# # [1, 4, 9, 25]
# arr_2 = sorted([i**2 for i in arr if isinstance(i, int)])
# arr_2.pop(1)
# print(arr_2)
import random
import sys
import time


import requests as REQ
import re
from bs4 import BeautifulSoup

# n = 3405100
# n1 = ''.join(reversed(str(n)))
# print(n1)
# arr = [i for i in n1]
# arr2 = [ ]
# for i in arr:
#     if i
# print(arr)
# a,n = None,0
# arr = []
# def Foo(arg):
#     arr.append(arg)
# while 1:
#     a, *b= input().split()
#     if b and b[0].isdigit():
#         b = int(''.join(b))
#         match a,b:
#             case 'add', b: n += b
#             case 'minus', b: n -= b
#             case 'mul', b: n *= b
#             case 'div', b: n //= b
#     if not b:
#         match a:
#             case 'zero': n *= 0
#             case 'result': Foo(n)
#             case 'exit':
#                 for i in arr: print(i)
#                 exit()

# s = 'Moscow'
# uni = [ord(i) for i in s]
# print(uni)
# uni_str = ''.join([str(i) for i in uni])
#
# uni_chr = [chr(i) for i in uni]
# print(''.join(uni_chr))
# print(uni_str)
# #русская


# import string
# # s, step = input(), int(input())
# alpha_list =  [i for i in string.ascii_lowercase]
# r = 4
# ords = [ord(i) + r for i in string.ascii_lowercase]
# print(ords)
#
# print(alpha_list)
#
# print(ord('a'))
# print(ord('d'))
# abc
# 3
# def

# aaabbb
# 2
# ccceee


# aaabbccccaaaab
# a
# 4


#
# s = 'eeeebbccccaaab'
# s_list = [i for i in s]
# couples = []
# num = 0
# for i in range(len(s)):
#     if i+1 != len(s) and s_list[i] == s_list[i+1]:
#         num += 1
#     elif i+1 != len(s) and s_list[i] != s_list[i+1]:
#         couples.append([s_list[i],num + 1])
#         num = 0
#     elif i+1 == len(s):
#         couples.append([s_list[i],num + 1])
# print(couples)
# result_list = [i for i in couples if i[1] == max([i[1] for i in couples])]
# if len(result_list) == 1:
#     final_list = [j for i in result_list for j in i]
#     print(f'{final_list[0]}\n{final_list[1]}')
# else:
#     print(f'{result_list[-1][0]}\n{result_list[-1][1]}')

#
# numbers = [int(i) for i in input() if i.isdigit()]
# result = []
# res = 1
# for i in numbers:
#     if numbers[numbers.index(i)] == numbers[-1]:
#         break
#     result.append(numbers[numbers.index(i)] + numbers[numbers.index(i) + 1])
# print(*result)
#
# #___________________________________________
# numbers = [int(i) for i in input() if i.isdigit()]
# re = [i for i in enumerate(numbers)]
# p = 0
# result_2 = []
# for i in re:
#     if i == re[-1]:
#         break
#     if i[0] == p:
#         result_2.append(i[1] + re[p + 1][1])
#     p += 1
# print(' '.join([str(i) for i in result_2]))

# a = [1, 3, 4, 2, 100, -5, 6, 'sdgsg', True, 4.3]
# print(a)
# arr = list(map(lambda param: param ** 2 if isinstance(param, int) else param, a))
# print(arr)
# arr_2 = sorted([i for i in list(map(lambda param: param ** 2 if isinstance(param, int) else param, a)) if isinstance(i, int)])
# print(arr_2)
#
# a = [2,5,6,7,8]
# def Foo(num):
#     return num ** 2
# print(list(map(Foo, a)))

# a = 0
# b = 1
# if a ==0:
#     a += 1
#     print('0')
#
# elif b == 1:
#     print('1')
#
# arr = [1,1,2,3,4,5,6]
# dict_1 = {
# }
#
# for i in arr:
#     dict_1.setdefault(i, arr.count(i))
# for k,v in dict_1.items():
#     print(f'{k} {v}')
# print('\n')
# #----------------------------
# arr_2 = [f'{i} {arr.count(i)}' for i in arr]
# arr_3 = ['{} {}'.format(i, arr.count(i)) for i in arr]
# print(arr_2)
# print(arr_3)
# for i in arr_2:
#     print(i)
# ---------
# def SETINPUT():
#     return set(input().split())
# required, optional, user_data = [SETINPUT() for i in range(3)]
# #Базовое решение для Бруснички
# if user_data.intersection(required) == required:
#     if user_data.issubset(required | optional):
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)
# #Более быстрое решение
# if user_data.intersection(required) == required:
#     print(True) if user_data.issubset(required | optional) else print(False)
# else:
#     print(False)
# ---------
# import json
# d = json.loads(input())
# arr = []
# for i in d:
#     for k,v in i.items():
#         if isinstance(v, dict):
#             for k2, v2 in v.items():
#                 if k2 == 'age':
#                     arr.append(v2)
#         if k == 'age':
#             arr.append(v)
# print(max(arr))
# -------------
# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# print(a|b)
# a.update(b)
# print(a)
# print(a.union(b))
# star = '*'
# space = ' '
# FULL = False
# num_space = 5
# num_star = 0
# for i in range(num_space*2 + 1):
#     print(f'{space * num_space}{star + star*num_star}')
#     if not FULL:
#         num_space -= 1
#         num_star += 2
#     if num_space < 0:
#         num_star = num_star - 2
#         #заранее убираем две звезды чтобы строка не повторялась
#         num_space = num_space + 1
#         #заранее делаем отступ чтобы не было двух одинаковых с трок с нулевыми отступами
#         FULL = True
#     if FULL:
#         num_space += 1
#         num_star -= 2
# class A:
#     def __init__(self):
#         ...
#     def mA(self):
#         print(1)
#     def mB(self):
#         A().mA()
#         print(2)
# a = A()
# a.mB()


# a = input().lower().split() #Казнить, нельзя.помиловать
# b, t, z = [], '.', ','
# for i in a:
#     if z in i or t in i:
#         if z and t not in i: b.append(i.replace(z, ''))
#         elif t and z not in i: b.append(i.replace(t, ' ').split())
# print(b)
# c = []
# for i in b:
#     if isinstance(i, list):
#         for j in i:
#             c.append(j)
#             continue
#         continue
#     else:
#         c.append(i)
# print(c)
# v = [j for i in b for j in i if isinstance(i, list) else i]
# print(v)
#
#
# print(c)
# import pprint
#
# #ввод
# arr = ['aaaa', 'bbbbbbb', 'ccda', 'eeee']
# #вывод
# dict_arr = {
#     'a': 4,
#     'b': 7,
#     '2': {'c': 2,
#           'd': 1,
#           'a': 1} ,
#     'e':4
#                 }
#
#
# arr2 = ['aaaa', 'bbbbbbb', 'ccda', 'eeee']
# dict_arr2 = dict()
# for i in arr2:
#     dict_arr3 = dict()
#     for j in i:
#         if i.count(j) == len(i):
#             dict_arr2.setdefault(j, i.count(j))
#             #не ставим окончание цикла так как каждый раз
#             # словарь перезаписывается от чего дублей и не будет
#         else:
#             dict_arr3.setdefault(j, i.count(j))
#             dict_arr2.setdefault(arr2.index(i), dict_arr3)
#
#
# for k, v in dict_arr2.items():
#     print(f'{k} {v}')
# print(f'\n')
#
# pp = pprint.PrettyPrinter(width=1)
# pp.pprint(dict_arr2)


#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 1 5 10 10 5 1

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1


#   1 3 3 1
#  1 4 6 4 1
# треугольник Паскаля
# max_l = 10
# arr = []
# idx = 0
# for i in range(max_l):
#     idx = 0
#     if len(arr) == 0:
#         arr.append([len(arr) + 1])
#         continue
#     else:
#         arr_2 = []
#         for i in arr[-1]:
#             if idx < len(arr[-1]) - 1:
#                 arr_2.append(arr[-1][idx] + arr[-1][idx + 1])
#             idx += 1
#             if idx == len(arr[-1]):
#                 arr_2.insert(0, 1)
#                 arr_2.insert(len(arr_2), 1)
#         arr.append(arr_2)
# space_len = len(arr[-1])
# space = ' '
# for i in arr:
#     element = ' '.join(map(lambda x: str(x), i))
#     print(f'{space * space_len}{element}')
#     space_len -= 1
# ----------------------------------------
# a = {
#     'Молоко': '2',
#     'Хлеб': '1'
# }
# for i in range(1):
#     product = input()
#     quantity = int(input())
#     if product in a and isinstance(a[product], str):
#         quantity = quantity + int(a[product])
#     a.update({product: quantity})
#
# print(a)
# --------------------------------------


# for i in arr2[0]:
#     if idx < len(arr2[0]) - 1:
#         arr3.append(arr2[0][idx] + arr2[0][idx + 1])
#     idx += 1
#     if idx == len(arr):
#         arr3.insert(0, 1)
#         arr3.insert(len(arr3), 1)
# print(ord('a'))
# print(int('0x30a0', base=16))
# i = 0
#
# for j in range(int('0x30a0', 16), (int('0x30a0', 16) + 96)):
#     print(ord('a'))
#     print(int('0x30a0', base=16))
#     i = 0
#
#     for j in range(int('0x30a0', 16), (int('0x30a0', 16) + 96)):
#         print(chr(j))
#     print(chr(j))
# arr = [1, 4, 6, 4, 1]
#
# #       1 4 6 4 1
# arr2 = []
# for i in range(len(arr)):
#     if i == len(arr) - 1:
#         arr2.insert(0, 1)
#         arr2.insert(len(arr), 1)
#         break
#     arr2.append(arr[i] + arr[i + 1])

# num = random.randrange(220, 660, 22)
# print(num)
# a = [-i for i in range(0, random.randrange(220, 660), 22)]
# print(a)
# #220 440 110 660 [0, 440, 22]
# print(a[random.randint(1,9):random.randint(9,len(a) + 1)])
# letters_y = [-i for i in range(0, 682, 22)]
# print(letters_y)
# new_let_y = letters_y[rnd.randint(1, 5):rnd.randint(5, len(letters_y))]
# print(new_let_y)

# a = [1,4,5,6,9]
# a = [i for i in range(1, 11)]

# arr = [rnd.choice(a) for i in range(rnd.randint(1, len(a))) if rnd.choice(a) not in arr]
# arr2 = [rnd.choice(a) for i in range(rnd.randint(1, len(a)))]
# print(arr2)
# arr = []
# [arr.append(i) for i in arr2 if arr.count(i) < 1]
# print(arr)
# for i in range(rnd.randint(1, len(a))):
#     AR = rnd.choice(a)
#     if AR not in arr:
#         arr.append(AR)
#     else: continue
#
# print(arr)
# #a = [1,2,3,4,5,6,7,8,9,10]
# arr = []
# for i in a:
#
#
#
# for i in range(5):
#     print(a)


#
# 0, 1, 1, 2, 3, 5, 8, 13
# def FIBO(num):
#     ...
# n = 8
# arr = []
# for i in range(n+1):
#     qwe = i + 1
#     if i < 1:
#         arr.append(i)
#         arr.append(i + 1)
#     else:
#        arr.append(arr[i] + arr[i-1])
# print(arr)


# def foo(n, flag):
#     if n <= 1:
#         return n
#     print(f'{n} {flag}\n\n')
#     return foo(n-2, 'left') + foo(n-1, 'right')
# print(foo(6, 'center'))


# class StackClass:
#     def __init__(self):
#         self.stack = []
#     def push_in(self, el):
#         self.stack.append(el)
#     def m(self):
#         return self.stack == []
# sc = StackClass()
# sc.push_in(10)
# sc.push_in(20)
# sc.push_in(90)
# sc.m()
# print(sc.stack)
# print(sc.m())


# ---------------бинарный поиск
# import random as rnd
# # num = int(input('Введите число'))
# #найти пятерку
# arr = list(map(lambda x: list(set(x)), [[rnd.randint(1,11) for i in range(10)] for j in range(3)]))
# flag = 0
#
# arr2 = [2, 3, 4, 5, 6, 7, 8, 10, 15,17, 18, 110 ,112, 200, 212]
# #miidle = 7 (индекс)
#
# step = 0
#
# def binary_search(lst, number):
#     start, end = 0, len(lst)-1
#
#     while start <= end:
#         middle = (start + end) // 2
#         # print(f'START {start}     значение {arr2[start]}\n'
#         #       f'END {end}          значение {arr2[end]}\n'
#         #       f'CENTER {middle}    значение {arr2[middle]}')
#         if number == lst[middle]:
#             return True
#         if number > lst[middle]:
#             start = middle + 1 #он уже не равен концу, а значит мы выходим из цикла
#         elif number < lst[middle]:
#             end = middle - 1
#         #..
#         # print(f' &&& {arr2[start:end]}\n')
#     return False
#
#
# num = 10
#
# def main():
#     coll = []
#     flag = 0
#     for ls in arr:
#         flag = flag + 1 if binary_search(ls,num) else flag
#         coll.append(arr.index(ls)) if binary_search(ls, num) else ...
#     coll = ','.join(list(map(lambda x: str(x), coll)))
#     print(f'Число {num} найдено в {flag} коллекциях под индексами {coll}') if flag else print(f'число не найдено')
# main()

# [[1, 2, 3, 5, 7, 8], [4, 5, 6, 7, 8, 9, 11], [1, 3, 5, 6, 7, 8, 9, 11]]
# ------------------------------
# num = 100
# def stars(arg_space, arg_stars):
#     print(f'{arg_space}{arg_stars}{arg_stars[:-1]}')
# for i in range(num - 1, 0, -1):
#     spaces = i - num // 2
#     num_new = num // 2
#     space_up = ' ' * spaces
#     stars_up = '*' * (num_new - len(space_up))
#     stars_down = '*' * i
#     space_down = ' ' * (num_new - len(stars_down))
#     if i > num // 2:
#         print(f'{space_up}{stars_up}{stars_up[:-1]}')
#     else:
#         print(f'{space_down}{stars_down}{stars_down[:-1]}')
#     # if i > num //2:
#     #     stars(space_up, stars_up)
#     # # print(f'{space}{stars_left}{stars_left[:-1]}')
#     # if i <= num // 2:
#     #     stars(space_down, stars_down)
#     # print(i)
import time

# def choose_plural(num, words):
#     remainder = num % 10
#     tens = int(str(num)[-2:])
#     #-------посложнее но покороче
#     # def not_tens():
#     #     if remainder == 1: return f'{num} {words[0]}'
#     #     return f'{num} {words[1]}' if 2 <= remainder <= 4 else f'{num} {words[2]}'
#     # def yes_tens():
#     #     return f'{num} {words[2]}'
#     # return not_tens() if not 11 <= tens <= 20 else yes_tens()
#
#
#     #----попроще но подлиннее
#
#     if not 11 <= tens <= 20:
#         if remainder == 1:
#             return f'{num} {words[0]}'
#         elif 2 <= remainder <= 4:
#             return f'{num} {words[1]}'
#         else:
#             return f'{num} {words[2]}'
#     else:
#         return f'{num} {words[2]}'
#
#
# #
# print(choose_plural(10000000001, ('банан', 'банана', 'бананов')))
# #
# # #print(choose_plural(54, (банан, банана, бананов))
# # #>>> 54 банана
# # arr = [1,2,3,4]
# # arr2 = [5,6,7,89]
# # arr3 = sum(arr, arr2)
# # print(arr3)


# letters = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# mess = 'Привет World'
#
#
# def encrypt(message_param, k):
#     new_message = ''
#     for i in message_param:
#         if i.upper() in letters:
#             new_message += letters[letters.index(i.upper()) + k]
#         else:
#             new_message += i
#

#     return new_message
# encrypt_message = encrypt(mess, 5)
# print(encrypt_message)
# word_size = [i*2 for i in range(11)][1:]
# colors_bg = [[0, i + 20, 0] for i in range(0, 200, 20)]
# bg_params = {
#
# }
# for k in zip(word_size, colors_bg):
#     bg_params.setdefault(k[0], k[1])
# print(bg_params)


# def func_calc(lst, n):
#     if n == 1:
#         print(lst)
#         return
#     for i in range(n):
#         func_calc(lst, n - 1)
#         if n % 2 == 0:
#             lst[i], lst[n-1] = lst[n-1], lst[i]
#         else:
#             lst[0], lst[n-1] = lst[n-1], lst[0]
# lst = [i for i in range(3)]
# func_calc(lst, len(lst))
# pass
# arr = [1,2, 3]
# r = 0
#
# print(arr)
# def Foo(arr, n, var):
#     if n == 1:
#         ...
#     for i in range(n):
#         Foo(arr, n-1, 0)
#         if not var:
#          print(n)

# if n == 1:
#     print(arr)
# for i in range(n(2)):
#     Foo(arr, n - 1)

# if n == 1:
#     print(arr) +++
# for i in range(n):
#     Foo(arr, n - 1)


# >>>>>>>>>> [0, 1, 2]
# [1, 0, 2]
# [2, 0, 1]
# [0, 2, 1]
# [1, 2, 0]
# [2, 1, 0]


# arr = [1,2,3]
# arr2 = []
# arr3 = random.sample(arr, len(
#     arr
# ))
# print(arr3)
# var = 0
# while True:
#     arr_n = random.sample(arr, len(arr))
#     if arr_n not in arr2:
#         arr2.append(arr_n)
#     else:
#
#         continue

# >>>>>>>>>> [0, 1, 2]
# [1, 0, 2]
# [2, 0, 1]
# [0, 2, 1]
# [1, 2, 0]
# [2, 1, 0]
# arr = [1,2,2,4,5]
#
# def Foo(arr):
#     for i in arr:
#         if arr.index(i) != len(arr) - 1 and arr[i] == arr[i+1]:
#             return False
#         return True
# print(Foo(arr))
# abc
# cba bac acb
#
#
# axiom = 'abc'
# gens = 3
# let1, chr1 = 'a', 'cba'
# let2, chr2 = 'b', 'bac'
# let3, chr3 = 'c', 'acb'
#
# def Foo(axiom):
#     res = ''
#     for i in axiom:
#         if i == let1:
#             res += f'{chr1} '
#         elif i == let2:
#             res += f'{chr2} '
#         else:
#             res += f'{chr3} '
#     return res
#
# for i in range(gens):
#     print(axiom)
#     axiom = Foo(axiom)

# ------######
# arr = []
# def Foo(num):
#     while num >= 1:
#         if num % 2:
#             arr.append(1)
#         else:
#             arr.append(0)
#         num = num // 2
# Foo(100)
# print(''.join(map(lambda x: str(x), reversed(arr))))
# --------#######
# class Stack:
#     def __init__(self):
#         self.elements = []
#     def push_in(self, element):
#         self.elements.append(element)
#     def show(self):
#         return self.elements
#     def is_empty(self):
#         return self.elements == []
# stack = Stack()
#
# print(stack.is_empty())
#
#
# def Foo(number):
#     stack = Stack()
#     while number >= 1:
#         if number%2:
#             stack.push_in(1)
#         else:
#             stack.push_in(0)
#         number = number // 2
#     print(''.join(map(lambda x: str(x), reversed(stack.show()))))
# Foo(100)

#
# letters = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#
# mess = 'привет, world!'.upper()
# mess2 = 'привет, world!'.upper()
#
# def encrypt(message, k):
#     new_mess = ''
#     for word in message:
#         if word in letters:
#             if k > 0:
#                 if k > len(letters[letters.index(word):]):
#                     new_k = k - len(letters[letters.index(word):])
#                     new_mess += letters[new_k]
#                 else:
#                     new_mess += letters[letters.index(word) + k]
#             else:
#                 if abs(k) > len(letters[:letters.index(word)]):
#                     new_k = abs(k) - len(letters[:letters.index(word)])
#                     new_mess += letters[-new_k]
#                 else:
#                     new_mess += letters[letters.index(word) + k]
#         else:
#             new_mess += word
#     return new_mess
# #
# print(encrypt(mess, 5))
# print(encrypt(mess2, -5))
# def Rec(arg):
#     if len(arg) == 1:
#
#         return arg[0]
#     print(arg[0])
#     return arg[0] - Rec(arg[1:])
# print(Rec([1,2,3,4,5]))
# Rec([1,2,3,4,5])
# 1 + Rec([2,3,4,5])
# 2 + Rec([3,4,5])
# 3 + Rec([4,5])
# 4 + Rec([5])
# -------------
# 5
# 4 + 5
# 3 + 9

# 1 - Rec([2,3,4,5])
# 2 - Rec([3,4,5])
# 3 - Rec([4,5]) это то, что возвращает функция в строке выше (именно ФУНКЦИЯ)
# 4 - Rec([5])
# --------------
# 5

# 4 - 5
# 3 + 1
# 2 - 4
# 1 + 2
# class A:
#     def __init__(self, x):
#         self.x = x
#     def __add__(self, other):
#         return other + self.x
# a = A(10)
# a2 = A(20)
# print(a)
# print(a2)
# t = a.x + a2.x
# print(t)
# dict_1 = {'aww': 1, 'b1': 2, 'cqqqqqqqq': 3}
# list_from_dict = list(dict_1.items())
# print(list_from_dict)
# list_from_dict.sort(key=lambda x: x%10)
# print(list_from_dict)
# import hashlib
# hash_obj = hashlib.sha1('пароль'.encode('utf-8'))
# h = hash_obj.hexdigest()
# print(h)
# import hashlib
# # print(hashlib.algorithms_available)
# # print(hashlib.algorithms_guaranteed)
# a = hashlib.md5('Hello'.encode())
# # a2 = hashlib.md5(b'Hello')
# print(a.hexdigest())
# # print(a2.hexdigest())
# from uuid import uuid4
#
# salt = uuid4()
# print(salt)
# arr = []
# def Fibo(n):
#     if n < 2:
#         return n
#     arr.append(n)
#     return Fibo(n - 1) + Fibo(n - 2)
# print(Fibo(8))
# print(arr)
# n = 0
# arr = []
# while n != 8:
#     if not n:
#         arr.append(n)
#         arr.append(n + 1)
#     arr.append(arr[-1] + arr[-2])
#
#
#     n += 1
# print(arr)
# def memorize(func):
#     def wrapper(n, memory):
#         memory = dict(memory)
#         r = memory.get(n)
#         if not r:
#             r = func(n)
#             memory[n] = r
#         return r
#     return wrapper
#
# # @memorize
#
#
#
# def f(n):
#     if n < 2:
#         return n
#     return f(n - 1) + f(n - 2)
# print(f(n))

# arr = [1,2,3]
# print(*arr)
# def drag(func):
#
#     def wrap(*args, **kwargs):
#         var =
#         return func(*args, **kwargs)
#
#
#
#     return wrap
#
#
import string
import random

# a, num = [], 0
# for i in range(10):
#     a.append(i)
# print(a)

# def Foo(lst, el):
#     if len(lst):
#         return lst
#     lst.append(el)
#     el += 1
#     return Foo(lst, el)
#
# print(Foo(a, num))

# d = {
#
# }
# # for i in range(10):
# #     d.setdefault(random.choice(string.ascii_uppercase) * 2, random.randint(1, 100))
# # print(d)
# def Foo(arg_dict):
#     if len(arg_dict) == 10:
#         return arg_dict
#     arg_dict.setdefault(random.choice(string.ascii_uppercase) * 2, random.randint(1, 100))
#     return Foo(arg_dict)
# print(Foo(d))
# print(d)
# import time
# import random
# def dec_func(func):
#     def wrapper(*args):
#         start = time.time()
#         var = func(*args)
#         end = time.time()
#         print(f'время работы функции {func.__name__}составило {end - start}')
#         return var
#     return wrapper
#
#
# @dec_func
# def sum_number(a, b):
#     return a + b
# print(sum_number(5, 10))


# def time_dec(func):
#     def wrapper(*args):
#         start = time.time()
#         var = func(*args)
#         end = time.time()
#         print(f'Время работы функции {func.__name__}: {(end - start).__round__(10)} секунд')
#         return var
#     return wrapper
#
#
# @time_dec
# def push_lst(arg_lst, num):
#     arg_lst.append(num)
#     return arg_lst
# push_lst([], 15)

# def time_dec(func):
#     def wrapper(*args):
#         start = time.time()
#         var = func(*args)
#         end = time.time()
#         print(f'Время работы функции {func.__name__}: {(end - start).__round__(10)} секунд')
#         return var
#     return wrapper
#
#
# @time_dec
# def push_lst(arg_lst, num):
#     for i in range(num):
#         element = random.randint(1, num)
#         arg_lst.append(element)
#     return arg_lst
# push_lst([], 10)

# class Car:
#     def __init__(self, color, speed, mark):
#         self.color = color
#         self.speed = speed
#         self.mark = mark
#     def drive(self):
#         if self.mark == 'Toyota':
#             print(f'Машина {self.mark} едет со скоростью {self.speed}')
#         else:
#             self.speed = self.speed * 2
#             print(f'Неизветсная машина едет со скоростью {self.speed}')
#
# car = Car('red', 60, 'Toyota')
# car.drive()
# import urllib.request as UR
# webURL = UR.urlopen('https://ru.wikipedia.org/wiki')

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

# import requests
# r = requests.get('https://pythonpip.ru')
# print(r)
# import chardet
# import urllib.request
# data = urllib.request.urlopen('https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwjh9o6-uf2AAxUxDRAIHWqwDGIQPAgJ')
# print(data.read())
# from timeit import Timer
# def Foo():
#     arr = []
#     for i in range(100):
#         arr = arr + [i]
#     return arr
# print(Foo())
# arr = [i for i in range(1000)]
# arr2 = list(map(lambda x: x*2, arr))
# print(list(range(1000)))
#
# t1 = Timer(stmt="test_concat()", setup="from main import test concat")
# print("list concat , t1.timeit (number=1000),seconds")

# statements = ['[el*el for el in elems]',
#               '''res=[]
#               for el in elems:
#               res.append(el*el)''',
#               'map (lambda el: el*el, elems)']
# for i in statements:
#     print(i)

# def deco(func):
#     def wrapper(*args):
#         print(args[0] * 10)
#         print('я декоратор')
#     return wrapper
#
# @deco
# def Foo(n):
#     print(n*2)
#     print(f'я функция')
# Foo(10)


# t1 = timeit.Timer(stmt='foo1', setup='from __main__ import foo1')
# for i in range(10):
#     print(t1.timeit(number=1))
# print(t1.repeat(3, 100))
# t2 = timeit.timeit(stmt='foo1', setup='from __main__ import foo1')
# print(t2)
# a = 0
# arr = []
# for i in range(100):
#     if i%2 == 0:
#         arr.append(i)
# setup = "elems=range(2000)"
# print(setup)
# statements = [
#     'i*2 for i in range(10)',
#     """arr = []
# for i in range(100):
#     if i%2 == 0:
#         arr.append(i) """
# ]
# for st in statements:
# #
# from timeit import repeat
# from timeit import default_timer
# STR_CODE = """
# l = []
# for i in range(1000):
#     l += [i]
# """
# # def func_10(nums):
# #     return [i for i in range(len(nums)) if not nums[i] % 2]
# print(repeat(STR_CODE, 'from __main__ import STR_CODE', default_timer, 3, 10))
# # print(repeat('func_10', 'from __main__ import func_10', default_timer, 3, 100))
# # res = repeat(, import_comp, default_timer, 3, 10000)
# # print(res)

# from timeit import repeat, default_timer
# def Foo1():
#     arr = [i**2 for i in range(100)]
#     return arr
#
# def Foo2():
#     arr_lam = list(map(lambda x: x**2, [i for i in range(100)]))
#     return arr_lam
#
#
# rep1 = repeat('Foo1', 'pass', default_timer, 3, 100, globals())
# rep2 = repeat('Foo2', 'pass', default_timer, 3, 100, globals())
# print(rep1)
# print(rep2)
# def Foo3(arr, num):
#     num -= 2
#     if num < 0:
#         return list(reversed(arr))
#     arr += [num]
#     return Foo3(arr, num)
# print(Foo3([], 10))
# def rev(num):
#     return ''.join(list(reversed([j for i in str(num) for j in i])))
#
#
# num = 1234
#
# def rev2(arr, num):
#     if not len(str(num)):
#         return ''.join(arr)
#     string_num = str(num)
#     arr.append(string_num[-1])
#     num = string_num.replace(string_num[-1], '')
#     return rev2(arr, num)
# print(rev2([], 1234567890))
# from timeit import default_timer, timeit
# import time
#
# def deco_time(func):
#     def wrapper(args):
#         start_time = default_timer()
#         func(args)
#         print('{0:.10f}'.format(default_timer() - start_time))
#     return wrapper
#
# @deco_time
# def gen_prime(x):
#     multiples = []
#     results = []
#     for i in range(2, x + 1):
#         if i not in multiples:
#             results.append(i)
#             for j in range(i*i, x+1, i):
#
#                 multiples.append(j)
#     return results
#
# print('{0:.10f}'.format(timeit('gen_prime(100)', 'pass', default_timer, 1, globals=globals())))
# 0,1,1,2,3,5,8,13,21,34
# def fibo(num, arr):
#     arr.append(0)
#     arr.append(1)
#     for i in range(num-2):
#         arr.append(arr[i] + arr[i+1])
#     print(arr)
# fibo(10, [])
# arr_2 = []
#
# arr = {}
# def deco(func):
#     global arr
#     def wrapper(num, memory = {}):
#         # res = func(num)
#         # memory[num] = res
#
#
#         # print(num)
#         res = memory.get(num)
#         if res is None:
#             res = func(num)
#             memory[num]=res
#
#         return res
#     return wrapper
#
#
#
# # @deco
# def fibo(num):
#     if num < 2:
#         return num
#     return fibo(num - 1) + fibo(num - 2)
# print(fibo(10))
#
# #0,1,1,2
#
# # def Foo1(string_num, num):
# #     if not num:
# #         return string_num
# #     string_num += str(num % 10)
# #     return Foo1(string_num, num // 10)
# #
# #
# # print(Foo1('', 1234))
# a = {
#     'a':1,
#     'b':10
# }
# res = a.get('c')
#
# print(a.get('c'))
from timeit import timeit as time_method
from timeit import default_timer
from timeit import repeat
# def dec(func):
#     arr = []
#     memory = {}
#     def wrapper(number):
#         # memory = {} if not memory else ...
#         # memory.setdefault(number, func(number))
#
#         memory[number] = func(number)
#         return memory
#         # if args in cache:
#         #     return cache[args]
#         # else:
#         #
#         #     cache[args] = func(*args)
#         #     print(cache)
#         #     return cache[args]#
#         # if memory is None:
#         #     memory = {
#         #                 }
#         # memory = memory | {number:func(number)}
#
#
#     return wrapper
#
#
#
# @dec
# def rev(num):
#     if not num:
#         return ''
#     return f'{str(num%10)} {rev(num//10)}'
# print(rev(123))
# t1_base = time_method()
# t2_base = ...
# t3_base =...
#
# print(1%10)
# print()

# from cProfile import run
# from sys import setrecursionlimit as SETREC
# from toolz import itertoolz
# import random
# SETREC(10000000)
# def Foo(num):
#     if num == 100:
#         return num
#     num += 1
#     print(num)
#     return Foo(num)

# a = 10
# a //= 7
# print(a)
# arr = [1,2,3,4,5,6,7,8,9,10]
# print(arr[::-1])
# def lst_len(lst):
#     return len(lst)
#
#
# def get_sum(lst):
#     while len(lst) > 1:
#         lst = list(itertoolz.partition(2, lst, pad = 0))
#         lst = list(map(lambda x: sum(x), lst))
#     return lst
#         # if i != len(lst) - 1:
#         #     var = lst[i] + lst[i + 1]
#         # else:
#
# def main():
#     test_arr = [i for i in range(101)]
#     print(sum(test_arr))
#     print(*get_sum(test_arr))
# # t = list(map(lambda x: list(x), list(itertoolz.partition(2, test_arr, pad = None))))
# # t2 = list(itertoolz.partition(2, test_arr))
# # print(t)
# # get_sum(test_arr)
#


# def get_sum_rec(lst):
#     if lst[0] == lst[-1]:
#         return lst[-1]
#     lst[-2] = lst[-1] + lst[-2]
#     return get_sum_rec(lst[:-1])
#
#
# arr = [1, 2, 3, 45]  # 51
# print(sum(arr))
# print(lst_len(arr))
# print(get_sum_rec(arr))
# arr2 = [1,2,3,4,5,67,8,90]
# last_el = arr2[-1]
# print(arr2[:arr2.index(last_el)])
# arr3 = list(map(lambda x: arr2[arr2.index(x)],arr2))
# print(f'af {arr3}')
#
# def Foo112(num):
#     print(num ** 2)
#
# arr = 'asfsaf'
# print(arr[:arr.index('f')])
# print(''.join(i for i in Foo112.__name__ if i.isalpha()))
import os
# print(os.listdir())
# with open('CATALOG.txt', 'r', encoding='utf-8') as file:
#     print(type(file.read()))
# #######################################
# import json
#
# cat = {
#        }
#
# with open('CATALOG.json', 'r', encoding='utf-8') as file:
#     lam_dump = lambda x: json.dump(x, open('CATALOG.json', 'w', encoding='utf-8'))
#     try:
#         cat = cat | json.load(file)
#         for i in range(3):
#             prod = input('Введите товар!: ')
#             quan = int(input('введите количество! '))
#             cat[prod] = cat[prod] + quan if prod in cat else cat.setdefault(prod, quan)
#         lam_dump(cat)
#     except json.decoder.JSONDecodeError:
#         product = input('Введите товар: ')
#         quantity = int(input('введите количество '))
#         cat.setdefault(product, quantity)
#         lam_dump(cat)
# print(cat)
#########################################
# string = 'dump()'
# string_w = ''.join([i for i in string[:string.index('(')]])
# print(string_w)

# def Foo(lst):
#     return [i for i in lst if i%2 == 0]
# print(Foo([1,2,3,4,5,6,7,8,9,10]))
#
# var = lambda lst: [i for i in lst if i%2 == 0]
# print(var([1,2,3,4,5,6,7,8,9,10]))
# def func_1(param):
#     return param ** 2
# print(func_1(10))
# var = lambda param, param2, param3: param + param2 + param3 ** 2
#
# print(var(10, 100, 1000))
import string

# d = {name: numbers for name, numbers in zip(['a', 'b'], [1, 2])}
# print(d)
# class A:
#     def __init__(self, x):
#         self.x = x
#     @staticmethod
#     def m(par):
#         return par ** 2
#     def __add__(self, other):
#         return A.m(self.x) + other
#
# a = A(10)
# b = A(11)
# # print(a + b.m(b.x))
# def Foo():
#     return 100
# def Foo2():
#     return 100
#


# def foo():
#     a = 100
#     return a
#
# def foo2():
#     b = 100
#
#     return b
# print(time_method('foo()', 'from __main__ import foo', number=1000) * 1000000)
# print(time_method('foo2()', 'from __main__ import foo2', number=1000) * 1000)


# def concat_test():
#     my_lst = []
#     for i in range(1000):
#         my_lst += [i]
#     return 100
#
# def append_test():
#     my_lst = []
#     for i in range(1000):
#         my_lst.append(i)
#     return 100
#
# print(time_method('append_test()', 'pass', default_timer, 1000, globals())* 1000)
# print(time_method('concat_test()', setup='from __main__ import concat_test', number=1000) * 1000)
# print(time_method('append_test()', setup='from __main__ import append_test', number=1000) * 1000)

# def our_func(x):
#     def inner_func(y):
#         return x + y
#     return inner_func
# closed = our_func(10)
# print(closed(5))


# from timeit import timeit as TM
# arr = [i for i in range(100)]
# for i in arr:
#     if i % 2 != 0:
#         i = i * 2
#     else:
#         i = i // 2
#
# for i in arr:
#     var = arr[1:]
#     match i % 2:
#         case :
#             i = i * 2
#             print(f'flag {i}')
#         case 0:
#             i = i // 2
#             print(f'2 flag {i}')
#
# print(type(0))


# from memory_profiler import memory_usage
# mem_1 = memory_usage()
#
# arr = list(i for i in range(100000))
# print(arr)
# mem_2 = memory_usage()
# print(mem_2[0] - mem_1[0])


# 0.3125
#
# arr = [i for i in range(100)]
# #
# # def func(el):
# #     if el % 2 == 0:
# #         return True
# #     else:
# #         return False
# #
# # def func2(el):
# #     if not el % 10:
# #         return True
# #     else:
# #         return False
# #
# arr_2 = list(filter(lambda s: s % 10 == 0, arr))
#
# print(arr_2)
# d = {
#     'a':10,
#     'b':20
# }
# #
# d2 = {k: v ** 2 for k,v in d.items()}
# print(tuple(range(1, 52, 10)))
# #(2 3 4) (22,
# t = (22,23,24,32,33,34,42,43,44)
# make_t = lambda start, end, step: list(range(start, end, step))
# ttt = [*make_t(22, 53, 10), *make_t(23, 54, 10), *make_t(24, 55, 10)]
# print(ttt)

# url = 'https://letpy.com/simple-html-example'
# page = REQ.get(url)
# print(type(page.text))
# soup_string = str(BeautifulSoup(page.text, 'html.parser'))
# pattern = ''.join(re.findall(r'(?s)Случайное число.*\d', soup_string))
# p = re.findall(r'\d+', pattern)
#
# result_num = ''.join([number for number in pattern if number.isdigit()])
# print(result_num)


# with open('soup.txt', 'w+', encoding='utf-8') as file:
#     file.write(soup_string)
# print('------------------------\n--------------------')
# result = soup.findAll('p', 'Случайное число')
# print('------------------------\n--------------------')
# print(result)
# result_new = list(map(str, result))
# print(result_new)

# for i in result:
#     num_re = re.findall('\d+', i)
#     if num_re:
#         print(num_re[0])

# print(page.text)
# print('------------------')
# print(page)
# random_number = []
# soup = BeautifulSoup(page.text, 'html.parser')
#
# print('------------------')
# arr = soup.findAll('strong')
# print(arr)
#
# # find = soup.findAll('<title')
# # random_number.append(find)
# # print(random_number)


# from memory_profiler import profile, memory_usage
#
# def deco(func):
#     def wrapper(*args):
#         m1 = memory_usage()
#         print(m1)
#         t1 = default_timer()
#         result = func(*args)
#         m2 = memory_usage()
#         print(m2)
#         t2 = default_timer()
#         time_diff = (t2 - t1).__round__(5)
#         mem_diff = (m2[0] - m1[0]).__round__(2)
#         print(f'функция {func.__name__} заняла {mem_diff} памяти\n{time_diff} времени')
#         return result
#     return wrapper
# @deco
# # @profile
# def foo():
#     arr = [i for i in range(10000)]
#     return arr
# foo()
# import numpy
# import pathlib
#
# from GeekBrains.Algorithms.Lesson6.Lesson6_1_1 import main
# a = [[1,2], [3,4], [5,6]]
# arr = numpy.array(a)
# print(arr)


# from collections import namedtuple
# from pympler import asizeof as AS
# profit = [namedtuple('companies', 'name, money') for i in range(3)]
# pr_s = []
# pr0 = profit[0](name='rog',
#                 money=['235', '345634', '55', '235'])
# pr_s.append(pr0)
# pr1 = profit[1](name='kop',
#                 money=['345', '34', '543', '34'])
# pr_s.append(pr1)
# pr2 = profit[2](name='lag',
#                 money=['235', '345634', '55345', '235'])
# pr_s.append(pr1)
# print(pr_s)
#
# for i in pr_s:
#     for j in i:
#         print(j)
#
# profits_1 = [['rog', ['235', '345634', '55', '235']], ['kop', ['345', '34', '543', '34']],
#                     ['lag', ['235', '345634', '55345', '235']]]
#
# print(AS.asizeof(profits_1))

#
# import string
# import random
# from pprint import pprint
# from collections import namedtuple
# from pympler import asizeof
# from sys import getsizeof
#
# letters = string.ascii_lowercase
# var = 10
# print(getsizeof(var))

#
#
# profits_1 = [['rog', ['235', '345634', '55', '235']], ['kop', ['345', '34', '543', '34']],
#                ['lag', ['235', '345634', '55345', '235']]]
#
# arr = []
# for i in range(10000):
#     name, numbers  = '', list(map(str, list(range(10))))
#     for j in range(random.randint(1, 4)):
#         name += random.choice(letters)
#     num = [''.join([random.choice(numbers) for _ in range(random.randint(1,4))]) for i in range(4)]
#     arr.append([name, num])
#
# print(
# )
#
# print(arr)
#
# names = string.ascii_uppercase
# num = string.digits
# tuple_comp = [namedtuple('companies', 'name, money') for i in range(len(arr))]
# pr_s = [tuple_comp[i](name = arr[i][0], money = arr[i][1]) for i in range(len(arr))]
#
# print(pr_s)
#
# print(asizeof.asizeof(arr))
# print(asizeof.asizeof(pr_s))


# pr_s = [tuple_comp[i](name=''.join([random.choice(names) for item in range(random.randint(1,4))]),
#                       money=[str(random.randint(1,9999)) for elem in range(4)]) for i in range(10)]


# for i in range(10000):
#     pr = tuple_comp
# pr0 = tuple_comp[0](name='rog',money=['235', '345634', '55', '235'])
# pr_s.append(pr0)
# pr1 = tuple_comp[1](name='kop',money=['345', '34', '543', '34'])
# pr_s.append(pr1)
# pr2 = tuple_comp[2](name='lag',money=['235', '345634', '55345', '235'])
# profits_1 = [pr0, pr1, pr2]
import numpy as np
from pympler import asizeof as AS

# names = string.ascii_uppercase
# a1 = [1,2,3,4,5]
# print()
# print(AS.asizeof(a1))
#
# a = np.array([1,2,3,4,5])
# print(AS.asizeof(a))
# profits_1 = []
# for i in range(10000):  # <- увеличено число компаний для большего взаимодействия с памятью
#     name = ''
#     for i in range(random.randint(1, 4)):
#         name += random.choice(string.ascii_uppercase)
#     moneys = [random.randint(1, 9999) for _ in np.arange(4)]
#     profits_1.append([name, moneys])


# profits_1.append([name, sum(moneys)])


# profits_2 = [[random.randint(1, 9999) for i in range(4)] for j in range(1000)]
# prrr = np.array([])
#
# for t in np.arange(1000):
#     profits_3 = np.array([random.randint(1,9999) for _ in np.arange(4)])
#     print(profits_3)
#     prrr = np.array([prrr], [profits_3])
#     break
# print(prrr[0])

#
#
#
# # a = np.append(profits_1, 1)
# # print(a)
# print(f'вес {AS.asizeof(profits_2)}')
# print(f'вес {AS.asizeof(profits_3)}')
# #было 1545624
# #стало 1680144


# names = string.ascii_uppercase
#
#
# def make_company():
#     make_name = lambda: ''.join([random.choice(names) for _ in range(3)])
#     return [make_name(), *[str(random.randint(1, 9999)) for _ in range(4)]]
#
#
# a_list = [make_company() for _ in range(10)]
# print(a_list)
# print()
# # [['a',1,2,3,4],['b',4,5,6,7]]
# a_np = np.array([make_company() for _ in range(1000)])
# qwe = np.array([list(map(int, data[1:])) for data in a_np])
#
# print(a_list)
#
#
# aqwe = [list(map(lambda x: int(x) if x.isdigit() else x, data)) for data in a_list]
# print(f'ааа {aqwe}')
# print(AS.asizeof(a_list) + AS.asizeof(aqwe))
# print(AS.asizeof(a_np) + AS.asizeof(qwe))
# print(AS.asizeof(a_np) + AS.asizeof(aqwe))
# var = 4
# a1 = np.array([['1', '2'],['3','4'],['5','6']])
# print(a1[(np.array([0, 0]), np.array([0, 1]))]) #возвращает индексы
# from memory_profiler import memory_usage
# from timeit import default_timer
#
#
# def deco(func):
#     def wrapper(*args):
#         m1 = memory_usage()
#         t1 = default_timer()
#         res = func(*args)
#         m2 = memory_usage()
#         t2 = default_timer()
#         mem_diff = m2[0] - m1[0]
#         time_diff = t2 - t1
#         print(f'занято памяти {mem_diff} MiB\n{time_diff.__round__(3)} времени')
#         return res
#     return wrapper
#
#
#
# @deco
# def foo():
#     arr = list(range(1000000))
#     return arr
# foo()
#
# print()
# @deco
# def foo_2():
#     arr_np = np.array([_ for _ in range(1000000)])
#     return arr_np
# foo_2()
#
# print(
#
# )
# print([str(random.randint(1, 9999)) for _ in range(4)])
# sys.setrecursionlimit(10002)
# a = list(range(10000))
# idx = 0
# rec = 0
# def Foo():
#     global rec
#     print(sys.getrecursionlimit())
#     def foo_1(arg_idx):
#         print(sys.getrecursionlimit())
#         global rec
#         if arg_idx == len(a):
#             return a
#         a[arg_idx] = str(a[arg_idx])
#         arg_idx+= 1
#         rec += 1
#         return foo_1(arg_idx)
#     print(foo_1(idx))
#     print(f'final {rec}')
# Foo()
# sys.setrecursionlimit(1004)
# a = 0
# def foo():
#     global a
#
#
#     if a == 1000:
#         print(a)
#         return
#     a += 1
#     return foo()
# foo()
# class Foo():
#     __slots__ = ('a', 'b')
#     def __init__(self):
#         self.a = 1
#         self.b = 10
# f = Foo()
# print(f.____)
# from string import ascii_lowercase, ascii_uppercase
# word = lambda: ''.join([random.choice(ascii_lowercase) for _ in range(random.randint(1,7))])
# words = ' '.join([word() for _ in range(random.randint(3,5))])
#
# slogan = random.choice(ascii_uppercase) + words
# print(slogan)
# from memory_profiler import memory_usage
# def deco(func):
#     def wrapper(*args):
#         m1, t1 = memory_usage()[0], default_timer()
#         print(m1)
#         res = func(*args)
#         m2, t2 = memory_usage()[0], default_timer()
#         print(m2)
#         print(f'Memory {m2-m1}\nTime {t2 - t1}')
#         return res
#     return wrapper
# x = 10
# @deco
# def foo1():
#     if x == 10:
#         print(True)
#     else:
#         print(False)
#
#
# foo1()
#
# @deco
# def foo2():
#     print(True) if x == 10 else print(False)
# foo2()
# import numpy, hashlib
# letters = string.ascii_uppercase
#
#
# name_user = str(random.choice(letters) * 3)
# password = hashlib.sha256(name_user.encode() + str(1).encode()).hexdigest()
#
#
# user = lambda: [str(random.choice(letters) * 3), hashlib.sha256(name_user.encode() + str(1).encode()).hexdigest()]
# b = numpy.array([user() for _ in range(10)])
# print(b)
# import numpy
# a = numpy.array([])
# for i in range(10):
#     a = numpy.append(a, ['a'])
# a = numpy.array(list(map(list, a)))
# print(a)
# print()
# b = numpy.array([['a'] for _ in range(10)])
# print(b)
import collections
# l = string.ascii_uppercase
# a = numpy.array([['a',2], ['b',4], ['c',10], ['a',3], ['b',4], ['c',8], ['d',10], ['a',3], ['c',2]])
# at = numpy.array([1,2,3,3,4])
# ttt = [1,2,3,3,4]
# dict_tt = {num:ttt.count(num) for num in ttt}
# print(dict_tt)
# dict_at = {num: numpy.count_nonzero(at==num) for num in at}


# print(numpy.count_nonzero(a))
# print(collections.Counter(a))
# aa = [['a',2], ['b',4], ['c',10], ['a',3], ['b',4], ['c',8], ['d',10], ['a',3], ['c',2]]
#
# ty = [i[0] for i in aa]
# t = [[i[0] * 2, i[1]] if ty.count(i[0]) > 1 else i for i in aa]
# print(t)
#
#
# for i in aa:
#     if 'a' in i:
#         print(aa.count(i))
#
# names = numpy.array([name[0] for name in a])
# print(names)
# ara = numpy.array(list(map(lambda x: [x[0] * 2 if x[0] == 'a' else x[0], x[1]], a)))
# #
# print(ara)
# keys= collections.Counter([i[0] for i in aa])
# for k,v in keys.items():
#     if v > 1:
#         print(k)
# print(q)


# aaa = [1,2,2,2,3,4]
# arew = list(map(lambda x: [x[0] * 2, x[1]], aa))
# arew2 = [i for i in aa if i[0]== 'a' and aa.count(i) > 1]
# max = max([aa.count(i) for i in aa])
#
# p = [i[0] for i in aa]
# pr = ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'a', 'c']
# # print(p)
# # print(collections.Counter(p).values())
# # print(collections.Counter(pr))
# print([aa.count(i) for i in aa])
# print(collections.Counter([aa.count(i) for i in aa]).values())
#     # if i[0] == 'a' and aa.count(i) > 1:
#     #     r.append([i[0] * 2, i[1]])
#     # else:
#     #     r.append(i)
#
# data = {'a':2, 'b':5, 'c':10}
# t = []
# for i in data.items():
#     t.append(i[1])
# print(t)

# f = numpy.array([i[0] + random.choice(l) for i in a if numpy.count_nonzero(a == i) > 1])
# at = []
# for i in a:
#     if numpy.count_nonzero(a == i[0]) > 1:
#         print(i[0])
#
# a_new = numpy.array(list(map(lambda x:)))
# print(at)
# first_el = numpy.array([i[0] for i in a])
# if numpy.count_nonzero(numpy.array([i[0] for i in a]) == 'a') > 1:
#     print(True)
# if collections.Counter(first_el)['a'] > 1:
#     print(collections.Counter(first_el)['a'])


# print(numpy.count_nonzero(a == 3))
# print(a)
# for i in a:
#     print(f'{i[0]} встречается {numpy.count_nonzero(a==i[0])} раз')
#
# b = numpy.array([1,1,2,2,2,2,3,4,5,5,4,5,6,3])
# print(f'количество двое в массиве b {numpy.count_nonzero(b == 2)}')
# print(numpy.count_nonzero(a==2))
# a_new = numpy.array([i * 2 for i in a if int(i) % 2 == 0])
# print(a_new)
import collections
# arr = [['a',2], ['b',4], ['c','a'], ['a',3], ['b',4], ['c',8], ['d',10], ['a',2], ['c',2]]
# print(numpy.count_nonzero(arr == ['a', 2]))
# for i in arr:
#     print(numpy.count_nonzero(arr == i))
#     if i[0] == 'a':
#         print(numpy.count_nonzero(arr == i[0]))

# arr2 = [1,1,1,2]
# if collections.Counter(arr2)[1] == 3:
#     print(True)
# else:
#     print(False)
#
# d = {'a':1000}
# print(d['a'])

# a = int(''.join(list(map(str, [random.randint(1, 1000) for _ in range(10)]))))
# print(a)
# import re
# a = 'R12'
# t = 2
# reg = int(''.join(re.findall(r'\d+', a)))
# print(reg)
# b = [i for i in a]
#
# print(b)

# var = int(input())
# if var == 10:
#     print('1')
# elif var == 20:
#     print('2')
# elif var == 30:
#     print('3')
#
# var_2 = {
#     10: '1',
#     20: '2',
#     30: '3'
# }
#
# print(var_2.get(20)
# n = 10
# for i in range(n):
#     print(i)
#     print(n)
#     print()
#     n -= 1
# dict_old = {'b':2, 'a': 3, 't': 10}
# new_dict = sorted(dict_old.items())
# d = {}
# d1 = dt = lambda x:
# def foo():
#     for i in new_dict:
#         d.setdefault(i[0], i[1])
# foo()
# print(d)
# print(new_dict)
# r2 = [('c', 3), ('d', 4), ('a', 1), ('b', 2)]
# rdict = {i[0]: i[1] for i in r2}
# print(rdict)
# rd = ('a', 10)
# rrr = {item[0]: item[1] for item in [rd]}
# print(rrr)
#
# test_dict = {
#     'a':10,
#     'c':100,
#     'b': 45
# }
#
# new_dict = {item[0]: item[1] for item in sorted(test_dict.items())}
# print(new_dict)
#
# test_dict_2 = {
#     'a':10,
#     'c':100,
#     'b': 45
# }
# new_dict_2 = sorted(test_dict_2.items())
# print(new_dict_2)
import string
# text = 'gdfgdfh tsdgasdgsadg. fsdtgr f fasf. uuigcfbvcb ff. gsdtgr'
# text_lst = text.split()
#
# text_new = ' '.join(list(map(lambda x:x.title() if text_lst[text_lst.index(x) - 1].endswith('.') or text_lst.index(x) == 0 else x, text_lst)))
# print(text_new)
# print(text.split())
# for i in text_lst:
#     word, i_idx = i, text_lst.index(i)
#     print(word[0])
#     if i_idx != 0 and text_lst[text_lst.index(word) - 1].endswith('.'):
#         word[0] = word[0].upper()
#     print(word)
# for i in range(len(text_lst)):
#     if i != 0 and text_lst[i - 1].endswith('.'):
#         text_lst[i] = text_lst[i].title()
#
#     print(text_lst[i])
# print(''.join(text_lst))
# i_idx = text_lst.index(i)
#
# if i_idx != 0 and text_lst[i_idx - 1].endswith('.'):

# print(text_lst)

# nums = [1,2,3,3,3,3,3,3]
# # tt_new = [i for i in enumerate(tt)]
# # print(tt_new)
# # print(list(enumerate(tt)))
# tt_new = ''
# for i in enumerate(tt):
#     lst_i = list(i)
#     if list(i)[0] == 0:
#         lst_i[1] = lst_i[1].upper()
#     print(lst_i)
#     tt_new += lst_i[1]
# print(tt_new)
#
#
#
# # print([list(i) for i in enumerate(tt)])
# # t_new = ''.join(list(map(lambda x: x[1]. , [list(i) for i in enumerate(tt)])))
# # print(t_new
# #
# #       )
# # tt = ''.join(list(map(lambda x: x.upper() if tt.index(x) == 0 else x, tt)))
# # print(tt)
# arr = list(range(12))
# def foo():
#     print(len(arr))
#     i = int(len(arr) / 2)
#     yield i
#
# print(foo())
# [7, 5, 8, 1, 7, 5, 6, 10, 2, 3]


# сортировка кучей
# arr = [5, 16, 8, 14, 20, 1, 26]
# art = [1,2,3,4,5]
# class BinTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# bin = BinTree(1)
# print(bin)
# bin.left = BinTree(2)
# bin.right = BinTree(3)
# bin.left.left = BinTree(4)
# bin.left.right = BinTree(5)
# # 1
# # 2
# # 4
# # 5
# # 3
# #
# for i in art:
#     x = BinTree(i)
#     print(x)
# def pre_order(node):
#     if node:
#         print(node.value)
#         pre_order(node.left)
#         pre_order(node.right)
# pre_order(bin)
#
# arr_2 = [1,2,3,4,5]
# print('######################')
#
#
# lst = ['aaaa', 'bb', 'ccccccccc', 'y', 'aaaaaaaaaa']
# lst_sort = list(sorted(lst, key=len))
# print(lst_sort)
# d = {k: len(k) for k in lst}
# print(dict(sorted(d.items(), key=lambda x: x[1])))
# arr = [1,2,3,4,5]
# arr_2 = [5,6,7,8,90]
#
# for i, j in zip(arr,arr_2):
#     print(i)

# def foo(num, aq):
#     aq.append(num)
#     if len(aq) >= 3:
#         print(aq)
#         return
#     print(aq)
#     left = foo(num*2, aq)
#     right = foo(num*2 + 1, aq)


# def foo2(num, left, right, aq):
#
#     aq.append(num)
#     if len(aq) >= 5:
#         print(aq)
#         return
#
#     left = num * 2
#     foo2(left, None, None, aq)
#     right = num * 2 + 1
#     foo2(right, None, None, aq)
#     aq.append(left)
#     aq.append(right)
# var= [1]
# def left(num):
#     var.append(num)
# def right(num):
#     num += 1
#     var.append(num)
#
# def foo3(num, aq):
#     l = num * 2
#     r = num * 2
#     left(l)
#     right(r)
#     num += 1
#
#
#
# foo3(1, [])


# right = foo(num*2 + 1, aq)
# aq.append(left)
# aq.append(right)
# return foo(num, aq)


# foo2(1, None, None, [])
# foo(1, aq)


# def deco(f):
#     def wrapper(*args):
#         res = f(*args) * 10
#         return res
#     return wrapper
# @deco
# def Foo(num: int):
#     print(num)
#     return num
#
#
# print(Foo(4))
# arr_test = [4,6,2,5,8,5,3,4,4,5,6,7]
# def foo(lst):...
#
# arr_test_new = list({i: arr_test.count(i) for i in arr_test}.keys())
# print(arr_test_new)
#
#
# for i in arr_test:
#     arr_test_new.append(i) if arr_test_new.count(i) < 1 else ...
# print(arr_test_new)
# from math import ceil
# from statistics import median
# arr_test = [14, -43, 100, -80, -40, 42, -57, 10, 8, -52, -31, 73, -39, -70, -6, 32, -12, 34, 37, -90, -48, 34, -6, 91, -52, -96, -95, 89, 45, 22, -92, -82, -30, 68, 84, -49, -6, 65, 3, -29, -30, 15, 45, -70, -22, -78, 91, 91, -85, 43, -93, 53, 82, -72, 8, 38, -72, -5, -84, 44, 61, 31, 5, -30, 93, -9, 99, 51, 75, 41, 38, -46, 48, -41, 3, 64, 56, -94, -69, -73, -25, -72, 65, -22, 57, -24, -94, -27, 64, 44, 95, -100, -33, 24, 67, -6, 79, -89, 35, 75, -30, -71, -20, 59, -82, -50, 100, -21, 38, 18, -16, -57, 90, 36, 50, 99, 31, -38, 6, 32, -73, 3, 98, -76, 30, 100, 32, -68, 27, 82, 53, 81, 65, 66, -95, -67, -27, 90, 73, -41, 88, -51, -43, 75, -86, -25, -27, -4, 86, -7, -81, 72, -33, 19, 91, 15, 34, 15, 32, -22, -92, -11, 45, -71, -58, -5, 75, -96, -47, -78, -68, 54, -26, -99, -15, -38, -73, -74, -26, 94, -98, 24, -81, 78, -85, 82, 13, 98, -65, 15, -95, 24, 72, 36, 37, -61, 42, -96, -2, -50, 14, 6, -90, 71, -17, -42, 68, -97, 77, 88, 0, 100, 60, 40, 10, 4, -51, 17, 20, 66, -49, 42, 63, -72, -8, 77, 51, -56, 79, -50, -13, 35, -90, -16, -55, -71, -48, 73, 28, -48, 51, 66, 45, 61, 24, 45, -100, -74, 54, 96, 10, -69, -15, -97, -20, -16, -45, -39, -90, 63, 65, -82, 59, -28, 60, 50, 48, -31, 99, -46, -26, -25, -50, -75, -23, -42, -31, 58, -73, -21, -76, 75, -81, 53, 41, -71, -55, 65, -99, -57, 67, 96, 85, 49, -26, -70, 0, 55, 53, -63, -79, -68, -6, 61, 21, 61, 23, -86, -33, -27, -20, 44, 73, -22, -37, -74, -98, -9, -81, 95, -36, 21, -30, 13, -3, -54, -80, 94, -15, 56, -87, 92, -22, 10, -61, 11, 80, 6, 25, -26, -70, 3, 83, 62, 28, 11, 92, 38, -74, -33, -78, -8, -58, 77, -86, 14, 39, 6, -65, 23, 80, 15, 96, -91, 6, -59, -56, -8, 90, 68, 27, 25, 16, 89, -30, -20, 79, 75, -61, 62, 58, 57, 51, -75, -9, -59, -58, -33, 3, -78, -89, 69, 20, 95, -19, 38, 26, -18, 83, 87, 14, -97, -47, -29, -69, 46, 16, 24, 77, -39, -37, 50, 26, 74, -30, -11, -14, 52, -68, 85, -2, 1, 62, 12, -68, -96, -26, 10, 58, -39, -79, 13, -64, -64, 21, -32, -25, -46, -55, -39, -22, -96, 17, 81, 62, 98, -5, 27, 69, 59, 35, 6, -76, 21, 87, -16, -61, 37, 87, 86, -86, -94, 85, 43, 55, 17, -64, -57, -45, -22, 49, -74, 96, 30, -9, 80, 42, 87, 49, -11, 0, 77, -9, -91, 46, 64, 39, -46, -28, 16, 8, -11, 7, 84, -35, -26, 10, -62, -13, -60, 27, 30, -33, -17, 83, 70, -93, 32, -14, 40, -47, 24, 24, 4, 11, -48, -24, 77, -3, 63, -88, 70, 58, 83, 80, 40, 17, -80, 11, 51, -53, 88, -81, -39, -95, 44, -75, -79, 77, 72, -7, 29, 96, 64, 99, 10, -76, -57, 78, -82, 41, 93, 68, 52, 21, -91, 52, -13, -66, -30, -89, 8, 95, -77, 40, 6, -99, 1, 35, 91, 28, 74, -82, -9, -25, -48, 88, -86, -88, 77, -55, 11, -23, 19, -87, -17, -98, -91, -94, 19, 33, 12, 44, -74, 80, -91, -7, 60, 76, -42, -8, -47, -79, 4, -60, -43, -11, 27, 51, 76, 63, 17, 44, -47, 20, 19, 25, -81, 37, 49, 66, 5, 60, 80, -42, -11, 50, -62, 84, -44, 4, 82, 34, 87, -31, -63, 20, -32, 42, 48, 86, 66, -40, 89, -76, -95, -30, -28, -35, -62, -51, 33, 67, -26, 43, -40, -1, 59, 27, 18, -49, -65, -98, -75, 24, -4, 42, 64, 4, 41, -77, 28, 43, -62, -54, -86, -61, 22, -43, -98, 30, 58, 91, 99, 43, -61, -12, 89, 9, -24, -23, -85, -40, -30, 28, -67, -3, 40, 41, -52, 97, -28, -34, 23, -33, 28, 61, 62, -27, 62, -43, 12, -89, 19, -29, 44, -8, -25, -31, 78, -39, -59, -97, 80, -51, 92, 27, 91, 9, -88, -14, -45, 8, 100, -43, -36, 65, 62, -70, -22, -12, 96, -49, -49, -81, 71, 63, -45, -27, 46, -33, -80, 58, 81, 84, 68, -53, 97, -9, -79, 84, 46, 90, -86, 20, 17, 7, -47, 50, 35, -17, -83, -64, 99, -91, 2, -57, -10, -87, 19, -67, 94, 3, -18, 46, 2, 60, 73, -25, 55, 66, 52, 21, 51, 78, -16, 26, -13, -22, 38, 65, 91, -65, -68, 48, -65, 51, 28, 25, 78, -28, -19, -79, 36, -24, -9, -18, 12, -30, 94, -53, 71, 79, -28, 95, 88, 14, -99, -67, 45, 43, 32, 53, 4, 56, 65, 70, -26, -44, -10, -53, -50, -10, -54, -26, 80, -2, 86, 49, 97, 41, 62, 92, 56, -72, 65, -15, 1, -96, 88, -77, 98, 93, -78, -74, 6, -49, -73, 31, -15, 84, 75, -47, 14, 3, -74, 53, 76, 54, 92, -58, 73, -47, -12, -5, 11, 96, -8, -67, 23, 28, -26, 7, 77, 40, -85, 10, 79, 3, 62, 10, 18, 24, 78, 20, -22, -87, -59, -65, -42, 45, 47, 10, 56, -30, -21, 97, 26, -2, 37, 94, -90, 30, -33, -40, 40, -57, 15, -60, 73, 13, -56, 28, 14, -13, 46, 86, -59, 23, 63, -84, 55, 77, 21, -22, 80, -82, -29, 59, 53, -35, -22, 99, -48, -77, -67, -64, -43, 32, -39, 21, 39, 69, -2, 81, 5, -19, 8, 61, 35, 68, 81, -2, 34, -46, -23, -51, -21, 28, -34, -55, -1, 21, 18, -16, 3, 48, 28, -95, -92, -90, 32, 44, -24, -7, 54, 43, -60, -64]
# print(len(arr_test))
# print(f'медиана {median(arr_test)}')
# med = ceil(sum(arr_test) / len(arr_test)) #округление в большую сторону
# print(med)
#
# lst =  [14, -43, 100, -80, -40, 42, -57, 10, -79, 8, -52]
# def not_sort(lst):
#     half = ceil(len(lst) / 2)
#     while len(lst) > half:
#         lst.pop(lst.index(min(lst)))
#     return f'медиана = {min(lst)}'
# print(not_sort(lst))
#
#


# # Гномья сортировка
# def gnome_sort(lst: list)->int():
#     # arr = [random.randint(-100, 100) for _ in range(2 * m + 1)]
#
#     idx = 0
#     while 1:
#         if idx == len(lst) - 1:
#             break
#         if lst[idx] <= lst[idx + 1]:
#             idx += 1
#         else:
#             lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
#             idx = idx - 1 if idx > 0 else 0
#     arr_sort = list(sorted(lst))
#     print(f'Массив отсортирован!\n{lst}') if lst == arr_sort else ...
#     print(f'Медиана = {lst[len(lst) // 2]}')
#     # для 10 элементов : Время: 0.103
#     # для 100 элементов: Время: 0.105
#     # для 1000 элементов:Время 0.263, память: 0.09375 MiB
#     return
#
# print(median(arr_test))
# # print(gnome_sort(arr_test))
#
#
# #################### сортировка Шелла
#
# print('#######')
#
#
# #
#
# def shell_sort(lst):
#     # lst = [random.randint(-100, 100) for _ in range(2 * m + 1)]
#     N = len(lst)
#     dist = N // 2
#     i = 0
#     sort_var = False
#     while True:
#         if dist < 1:
#             break
#         if i + dist > len(lst) - 1 and sort_var:
#             # для прохода первых трех чисел если последовательность нечетная.
#             # если i + расстояние до следующего элемента группы больше последнего индекса, то возвращаем i значение нуля
#             # потом проходим еще раз, чтобы на всякий случай проверить первый элемент и центральный.
#             # 1. Возвращаем ложное значение элементу sort_var.
#             # ---идем по циклу---
#             # 2. Если 1 и центральный элементы поменялись, делаем истинным значение sort_var
#             # ---идем по циклу---
#             # 3. Возвращаемся к верхнему условию if. Снова делаем sort_var ложной и снова идем по цилку.
#             # 4. Когда мы пройдем по циклу с декущим значением dist(расстоянием) то сортировок уже не будет( так как все,
#             # что можно отсортировать - мы уже отсортировали). У нас останется ложным значение sort_var.
#             # 5. Попадаем в условие elif в конце и переходим на следующий проход уменьшая расстояние в два раза
#             sort_var, i = False, 0
#         elif i + dist > len(lst) - 1 and not sort_var:
#             dist, i = dist // 2, 0
#         if lst[i] <= lst[i + dist]:
#             i += 1
#         else:
#             sort_var = True
#             lst[i], lst[i + dist] = lst[i + dist], lst[i]
#             i += 1
#     print(lst)
#     print(f'Медиана = {lst[len(lst) // 2]}')
# # # shell_sort(arr_test)
#
#
# while True:
#     n = int(input('Введите число: '))
#     if n > 0 and n < 10:
#         print(n ** 2)
#     elif n > 10 and n < 100:
#         print(n * 2)
#         continue
#
#     print(f'dafgsdagasdgasg')
#     print('adfgdsagasdgasdg')
#     print([i for i in range(100)])


# var = 'beep boop beer!'
# print(list(map(lambda x: var.count(x), var)))
# var_new = list(sorted(var, key=lambda item: var.count(item)))
#
# print(var_new)
# d = {let: var.count(let) for let in var}
# print(d.keys())
import re

# s = [1]
# d = {
#     'a': lambda : s.append(10),
#     'b': lambda : s.append(1000)
# }
#
# # d2 = {
# #     'a': 10,
# #     'b': 100
# # }
# d.get('a')()
# print(s)
# from collections import Counter, deque, defaultdict
# import heapq
#
# arr = [0, 2, 6, 5, 1, 3, 4]
# heapq.heapify(arr)
# print(arr)
#
#
# s = 'beep boop beer!'
# # arr = [['r', 2, 'i'], [
# arr = [4, arr[0] * 2]
#
# symbols = dict(Counter(s))
# symbols_sort = dict(sorted(symbols.items(), key=lambda x:x[1]))
#
# letters = [list(i) for i in symbols_sort.items()]
# print(letters)
# print(symbols_sort)

# word = 'beep boop beer!'
#
# word_count = Counter(word)
# print(word_count.items())
# word_count_sort = dict(sorted(word_count.items(), key=lambda item: item[1]))
# arr = [list(i) for i in word_count_sort.items()]
# #[['r', 1], ['!', 1], ['p', 2], [' ', 2], ['o', 2], ['b', 3], ['e', 4]]
# print(arr)
# arr[0] = [arr[0][0] + arr[1][0], arr[0][1] + arr[1][1]]
# arr.pop(1)
# print(arr)
# #deque(['r', '!', 'p', ' ', 'o', 'b', 'e'])
# print(word_count_sort)


# [1, 1, 1, 3, 3, 4, 4, 5, 5, 5]
# print(arr_count)
# print(list(sorted(arr)))
# print(arr.count(min(arr)))
# minel = min(arr)
# arr_new = list(map(lambda x: arr.pop(arr.index(x)) if x == minel else x, arr))
# print(arr)
# print(arr_new)


# txt = 'beep boop beer!'
# d = defaultdict(int)
# for i in txt:
#     d[i] += 1
# print(d)
# import heapq
# from collections import defaultdict
#
#
# # Создание класса для узла дерева Хаффмана
# class Node:
#     def __init__(self, char, freq, left=None, right=None):
#         self.char = char  # символ
#         self.freq = freq  # частота символа
#         self.left = left  # левый потомок
#         self.right = right  # правый потомок
#
#     # Оператор сравнения для узлов
#     def __lt__(self, other):
#         return self.freq < other.freq
#
#
# # Функция для создания таблицы частот символов в тексте
# def get_frequency(text):
#     freq = defaultdict(int)
#     for char in text:
#         freq[char] += 1
#     print(f'fadfafd {freq}')
#     return freq
#
#
# # Функция для построения дерева Хаффмана
# def build_huffman_tree(freq):
#     print(f'{freq}')
#     heap = []
#
#     for char, f in freq.items():
#         heapq.heappush(heap, Node(char, f))
#     print(f'flag {heap}')
#     while len(heap) > 1:
#         left_node = heapq.heappop(heap)
#         right_node = heapq.heappop(heap)
#         merged_node = Node(None, left_node.freq + right_node.freq, left_node, right_node)
#         heapq.heappush(heap, merged_node)
#
#     return heap[0]
#
#
# # Функция для кодирования символов на основе дерева Хаффмана
# def encode(node, code='', codes={}):
#     if node.char:
#         codes[node.char] = code
#     else:
#         encode(node.left, code + '0', codes)
#         encode(node.right, code + '1', codes)
#     return codes
#
#
# # Функция для сжатия текста с использованием таблицы кодов
# def compress(text, codes):
#     compressed_text = ''
#     for char in text:
#         compressed_text += codes[char]
#     return compressed_text
#
#
# # Функция для декодирования сжатого текста
# def decompress(compressed_text, node):
#     decoded_text = ''
#     current_node = node
#     for bit in compressed_text:
#         if bit == '0':
#             current_node = current_node.left
#         else:
#             current_node = current_node.right
#         if current_node.char:
#             decoded_text += current_node.char
#             current_node = node
#     return decoded_text
#
#
# # Пример использования алгоритма
#
# text = "Hello, World!"
#
# # Создание таблицы частот символов
# freq = get_frequency(text)
#
# # Построение дерева Хаффмана
# huffman_tree = build_huffman_tree(freq)
#
# # Создание таблицы кодов символов
# codes = encode(huffman_tree)
#
# # Сжатие текста
# compressed_text = compress(text, codes)
# print("Сжатый текст:", compressed_text)
#
# # Декодирование сжатого текста
# decoded_text = decompress(compressed_text, huffman_tree)
# print("Декодированный текст:", decoded_text)
# arr22 = deque([('r', 1), ('!', 1), ('p', 2), (' ', 2)])
# d = {
#     0: arr22.popleft(),
#     1: arr22.popleft()
# }
# print(arr22)
# print(d)

# d = {
#
# }
# k2 = {0:
#           {0:
#                {0: 'b', 1: 'a'},
#       1: {0: 'z', 1: 'y'}
#                             }}
#
#
k = {0:
         {0: {0: 'b', 1: 'a'},
          1: {0: 'z', 1: 'R'}},
     1:
         {0: 'c', 1: 'd'}
     }
# def make_bin_code(arg_d):
#     if isinstance(arg_d, dict):
#         zero_part = arg_d.get(0)
#         one_part = arg_d.get(1)
#         print(f'zero_part {zero_part}')
#         print(f'one_part {one_part}')
#         return make_bin_code(zero_part), make_bin_code(one_part)
#     else:
#         return arg_d
#
# print(make_bin_code(k))

# for k,v in k3.items():
#     if v == 'flag':
#         print(k)
k2 = {0:
          {1:
               {1:
                    {0:
                         {0: 'note', 1: 'flag'},

                     4:
                         {5: 'witcher'}}}}}

tree = {1:
            {0: 'b',
             1: {0: ' ',
                 1: 'o'}},

        0:
            {0:
                 {0:
                      {0: 'r',
                       1: '!'},
                  1: 'p'},

             1: 'e'}}

tree2 = {0:
             {0: 'b',
              1: {0: 't',
                  1: 'o'}},
         1: {0: 'c'}
         }
# o 411
# print(list(tree.items())[0])
code = ''
word = '!'
var = 0
# while not var:
#     for k, v in tree2.items():
#         if isinstance(v, dict):
#             code += k.__str__()
#             tree2 = v
#         else:
#             if v == word:
#                 code += k.__str__()
#                 print(code)
#                 var = 1


# code_table = {
#
# }
# def foo(el, code):
#     if not isinstance(el, dict):
#         code_table.setdefault(el, code)
#         print(code_table)
#         print(f'код Хаффмана {code} {el}')
#         return
#     foo(el.get(0), code= code + '0')
#     foo(el.get(1), code= code + '1')
#
# foo(tree, '')
# print(code_table)
# arr = ['1', '2', '3', '4']
# print(arr)
# arr[:2].append('888')
# class Car:
#     def __init__(self):
#         self.color = 'RED'
#     def met(self):
#         print(self.color * 10)

#
#
#
# arr = [random.randint(0, 100) for i in range(50)]
# print(f'искомый список')
# def sort_func(lst): #максимально неудобный способ сортировки, но я все равно сделал
#     for i in range(len(arr)):
#         slice = arr[i:]
#         min_slice = min(slice)
#         if arr.count(min_slice) > 1:#если встречаются дубли то воспользуемся разницей длин между срезом и исконным списком
#             idx_in_arr_from_slice = (len(arr) - len(slice)) + slice.index(min_slice)
#             first_in_arr_from_slice = len(arr) - len(slice)
#             # Меняем в исконном списке элементы местами, индексы которых находим в срезе на текущей итерации цикла.
#             # Это первый элемент среза и минимальный. Делается это для того, чтобы у нас не брался постоянно первый дублированный индекс элемента.
#             arr[first_in_arr_from_slice], arr[idx_in_arr_from_slice] = \
#                 arr[idx_in_arr_from_slice], arr[first_in_arr_from_slice]
#         else:
#             idx_min_arr = arr.index(min_slice)
#             arr[i], arr[idx_min_arr] = arr[idx_min_arr], arr[i] #
#         print(arr)
#         print()
#
# sort_func(arr)
#
#
# lst = [1,3,4,4,5,4,6,7]
# [[lst.remove(i) for i in lst if i == 4] for i in range(2)]
# print(lst)
import time

# def foo_deco():
#     def deco(f):
#         def wrapper(*args):
#             res = f(*args) * 10
#             print(res)
#             return res
#
#         return wrapper
#     @deco
#     def foo(x):
#         x += 1
#         return x
#
# def foo(x):
#
#     x += 1
#     print(x)
#     if x == 10:
#         foo_deco()
#         return
#     return x
#
# num = 1
# while 1:
#     time.sleep(0.5)
#     foo(num)
# import asyncio
#
#
# async def Foo1(x):
#     print(x ** 2)
#     await asyncio.sleep(3)
#     print(f'{Foo1.__name__} завершилась')
#
#
# async def Foo2(x):
#     print(x ** 3)
#     await asyncio.sleep(3)
#     print(f'{Foo2.__name__} завершилась')
#
#
# async def main():
#     task1 = asyncio.create_task(Foo1(10))
#     task2 = asyncio.create_task(Foo2(14))
#     await task1
#     await task2
#
#
# asyncio.run(main())

# import asyncio
# async def func_1(x):
#     print(x ** 2)
#     await asyncio.sleep(2)
#     print(f'Работа {func_1.__name__} завершена')
#
# async def func_2(x):
#     print(x ** 3)
#     await asyncio.sleep(3)
#     print(f'Работа {func_2.__name__} завершена')
#
# async def main():
#     task1 = asyncio.create_task(func_1(4))
#     task2 = asyncio.create_task(func_2(5))
#     await task1
#     await task2
# if __name__ == '__main__':
#     asyncio.run(main())
from django.views.generic import TemplateView


# class newspage(TemplateView):
#     def met(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)
#
# n = newspage()
# n.met()
# сложный способ
# import string
# import re
# binary_code = '1000' #Ж 8
# let_numbers= [let_ord for let_ord in range(ord('а'), ord('я'))]
# lets = [chr(let) for let in let_numbers]
# lets_upper = list(map(lambda let: let.upper(), lets))
# result_alpha = list(map(lambda couple: list(reversed(couple)), list(map(list, list(zip(lets, lets_upper))))))
# result_alpha_final = list(map(lambda couple: ''.join(couple), result_alpha))
#
# result_alpha_final.insert(6, 'Ёё')
#
# def encode(binary_code, number, idx, number_dec):
#     if number < 0:
#         return number_dec
#     number_dec += int(binary_code[idx]) * 2 ** number
#     number -= 1
#     idx += 1
#     return encode(binary_code, number, idx, number_dec)
# number_let = encode(binary_code, len(binary_code) - 1, 0, 0)
# print(number_let)
#
#
# result_let = result_alpha_final[number_let - 1]
# print(result_let)
#
# print(result_alpha_final)
# простой способ
# decimal = int(binary_code, 2)
#
# symbol = 0
# collections_symbols = ''
# while True:
#     try:
#         sym = chr(symbol)
#         print(str(sym))
#         collections_symbols += str(sym)
#         symbol += 1
#     except UnicodeEncodeError:
#         break
# print(collections_symbols)
# res = re.findall(r'[А-яА-Я]', collections_symbols)
# print(res)
# простой способ


# ---------------------------------
# result = list(map(lambda num: num ** 3, [i for i in range(1, 1000, 2)]))
#
# def func(lst):
#     devision_by_7 = sum([number for number in lst if sum(list(map(int, [num for num in str(number)]))) % 7 == 0])
#     return devision_by_7
# print(func(result))
# # print(func(list(map(lambda num: num + 17, result))))
# print()
# len_result = len(result)
#
# for i in range(len_result):
#     result[i] += 17
#
# print(result)
# print(func(result))

# 1
# def factorial(n):
#     if n <= 1:
#
#         return n
#     else:
#         return (n * factorial(n - 1))
#     # number = n #5
#     # var = number - (n - 1) # 1
#     # mul = var + 1
#     # var *= mul
#
#
#
# print(factorial(5))


# 2
# def summation(n):
#     if n < 1:
#         return n
#     else:
#         return (n + summation(n - 1))
#
#
# print(summation(8))

# 3
# num = 0
# lst = [1,2,3,4]
# for i in lst:
#     if i % 2:
#         num += i
# print(num)
# print()

# def sum_odd(lis, idx, num):
#     if idx <= 0:
#         print(num)
#         return num
#     if lis[idx] % 2 == 0:
#         num += lis[idx]
#         idx -= 1
#         return sum_odd(lis, idx, num)
#     else:
#         idx -= 1
#         return sum_odd(lis, idx, num)
#
#
#
# sum_odd([1,2,3,4], 3, 0)

# sum_odd([1,2,3,4])    # 4
# sum_odd([1,2,3,4,5])  # 9
# sum_odd([1,2,4,6,8])  # 1
# sum_odd([])           # 0
# sum_odd([2,4,6,8])    # 0
# print()
# num = 0
# def sum_odd_2(lis):
#     global num
#     idx = len(lis) - 1
#     if idx < 0:
#         return
#     if lis[idx] % 2 == 0:
#         num += lis[idx]
#         return sum_odd_2(lis[:idx])
#     else:
#         return sum_odd_2(lis[:idx])
#
# sum_odd_2([1,2,3,4])
# print(num)


# num = 0
# def sum_odd_2(lis):
#     global num
#     print(lis)
#     idx = len(lis) - 1
#     if idx < 0:
#         return lis
#     if lis[idx] % 2 == 0:
#         lis[0] += lis[idx]
#         return sum_odd_2(lis[:idx])
#     else:
#         return sum_odd_2(lis[:idx])
#
# sum_odd_2([1,2,3,4])
# print(num)


# ------
# 4Напишите рекурсивную функцию sum_sub(list),
# которая будет принимать список целых чисел.
# Эта функция будет суммировать все нечётные числа и
# вычитать все чётные числа. В конце она будет возвращать получившееся значение

# sum_sub([1,2,3,4])   # -2
# sum_sub([1,2,3,4,5]) # 3
# sum_sub([1,3,5])     # 9
# sum_sub([2,4,6])     # -12
# sum_sub([99,10,10])  # 79
# n = 0
# def sum_sub(list):
#     global n
#     idx = len(list) - 1
#     if idx < 0:
#         return n
#     if list[idx] % 2:
#         n += list[idx]
#         return sum_sub(list[:idx])
#     else:
#         n -= list[idx]
#         return sum_sub(list[:idx])
#
#
# print(sum_sub([1,2,3,4]))
# -------
# 5Слова-палиндромы
#
# Слова-палиндромы — это строки, которые одинаково читаются с обеих сторон.
# Например: «aba», «abba», «abcba», «aaa», «ababa» и так далее.Напишите функцию is_palindrome(string),
# которая будет принимать строку и возвращать «True», если строка является палиндромом, и «False» во всех других случаях.

# is_palindrome('aba')     # True
# is_palindrome('abba')    # True
# is_palindrome('abcba')   # True
#
# is_palindrome('abc')     # False
# is_palindrome('abbb')    # False
# is_palindrome('abab')    # False


# def is_palindrome(string):
#
#     if len(string) <= 1:
#         print(f'Палиндром')
#         return True
#
#     let_1 = string[0]
#     let_2 = string[-1]
#
#     idx_1 = 0
#     idx_2 = -1
#
#     if let_1 == let_2:
#         return is_palindrome(string[idx_1 + 1:idx_2])
#     else:
#         print(f'Не палиндром')
#         return False
# is_palindrome('abba')


# 6 6) Палиндромы, игнорирующие пробелы
#
# Напишите функцию is_pal(string), которая будет принимать строку и возвращать «True»,
# если строка — палиндром (при этом игнорируя все пробелы), и «False» во всех других случаях.
# is_pal('aba')      # True
# is_pal('a____bba')   # True
# is_pal(' a z  a')  # True
#
# is_pal('ab a b')   # False
# is_pal('a a  ba')  # False
# is_pal('a z a a')  # False

# s = 'ddd  r'
# print(''.join(list(map(lambda x: x if x != ' ' else '', list(s)))))
#
# def is_pal(string):
#
#     if len(string) < 1:
#         return f'палиндром'
#     let_1, let_2 = string[0], string[-1]
#     idx_1, idx_2 = 0, -1
#
#     if let_1 == '_':
#         return is_pal(string[idx_1 + 1: ])
#     elif let_2 == '_':
#         return is_pal(string[:idx_2])
#     elif let_1 == let_2:
#         return is_pal(string[idx_1 + 1:idx_2])
#     else:
#         return f'не палиндром'
#
#
#
# print(is_pal('abb_____a'))

# -------------
# 7) Удаление гласных букв

# Напишите функцию remove_vowels(string),
# которая будет принимать строку и возвращать только согласные буквы.


# remove_vowels('apple')     # ppl
# remove_vowels('orange')    # rng
# remove_vowels('pear')      # pr
# remove_vowels('pineapple') # pnppl
# remove_vowels('durian')    # drn
# remove_vowels('banana')    # bnn
# import string
#
# lets = string.ascii_lowercase
# vowels = [let for let in lets if let == 'a' or let == 'e' or let == 'i' or let == 'o' or let == 'u']
# result= ''
#
# str_2 = 'apoopetteelt'
# res = ''.join(list(map(lambda let: let if let not in vowels else '',list(str_2))))
# print(res)
# def remove_vowels(string):
#     global result
#     if len(string) < 1:
#         result = result[::-1]
#         print(result)
#         return
#     last_let = string[-1]
#     if last_let not in vowels:
#         result += last_let
#         return remove_vowels(string[:-1])
#     else:
#         return remove_vowels(string[:-1])
#
# remove_vowels('apoopetteelt')
# 'apoopetteeltt'
# 'apoopetteel'
# --------
# lets = string.ascii_lowercase
# vowels = [let for let in lets if let == 'a' or let == 'e' or let == 'i' or let == 'o' or let == 'u']
# n = ''
# def foo(string):
#     if len(string) == 1:
#         return string
#
#     if string[0] not in vowels:
#         if len(string) == 2:
#             if string[1] not in vowels:
#                 return foo(string[0]) + foo(string[1:])
#             else:
#                 return foo(string[0])
#         else:
#             return foo(string[0]) + foo(string[1:])
#
#     else:
#         return foo(string[1:])
#     # else:
#     #     return foo(string[1:])
# print(foo('agdsgsopooasgdapple'))
# -------
# 8) Удвоенные буквы
#
# Напишите функцию double(string), которая будет принимать строки и
# возвращать другую версию строки, в которой все буквы будут удваиваться.
# double('apple')   # aappppllee
# double('orange')  # oorraannggee
# double('pear')    # ppeeaarr
# double('abc')     # aabbcc
# double('zz')      # zzzz

# сомнительное решение
# def double(string):
#     if len(string) == 1:
#         return string * 2
#     return double(string[0]) + double(string[1:])
#
#
#
# print(double('apple'))


# def my_double(string, idx):
#     if idx >= len(string):
#         return string
#     string, idx = string.replace(string[idx], string[idx] * 2, 1), idx + 2
#     return my_double(string, idx)
# print(my_double('apple', 0))
# sss = 'apple'
# sss = sss.replace(sss[-1], 'fasfaf')
# print(sss)

# 9Напишите функцию pascal(n), которая будет принимать
# положительные целые числа n и возвращать n-ую строку треугольника Паскаля.

# def pascal(n):
#     if n < 0:
#         return n
#     print(n)
#     return pascal(n - (n - 1))
# pascal(3)

# num = 5
#
# result = []
# #обычное решение
# #[[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
# for i in range(2):
#     result.append([1]) if not len(result) else result.append([1,1])
#
# for i in range(3, num + 1):
#     result_2 = []
#     idx = 0
#     for j in range(i - 2):             #отсекаем первую и последнюю единицы, их добавим позже. Работаем только с другими цифрами
#         result_2.append(result[-1][idx] + result[-1][idx + 1])
#         idx += 1
#     result.append([1, *result_2, 1])
#     print(result)

# рекурсивное решение
# пример
# [[1], [1,2], [1,2,3], [1,2,3,4]]
# result = []
# num = 4
# first_el = 1
# for i in range(2, num + 1):
#     result.append([1]) if not len(result) else ...
#     result_2 = []
#     for j in range(i):
#         result_2.append(result[-1][0] + j)
#     result.append(result_2)
# print(result)


# def test_recursion(num, lst):
#     if num < 1:
#         return lst
#
#
# num = 4
# test_recursion(3, [[1]])

# def rec(lst):
#     if len(lst) == 5:
#
#         return lst
#     lst.append(1) if not len(lst) else lst.append(lst[-1] + 1)
#     return rec(lst)
# print(rec([]))
# #[[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
#--------------------------------------------
# lst_len = 0
# def paskal(n):
#     def rec_out(lst_out):
#         if len(lst_out) == n:
#             return lst_out[-1]
#
#         if not lst_out:
#             lst_out.append([1])
#             lst_out.append([1,1]) if n > 1 else ...
#
#         def rec(lst, idx):
#             if len(lst) == len(lst_out) - 1:
#                 return lst
#             lst.append(lst_out[-1][idx] + lst_out[-1][idx + 1])
#             idx += 1
#             return rec(lst, idx)
#
#         lst_out.append([1, *rec([], 0), 1]) if n > 2 else ...
#         return rec_out(lst_out)
#
#     print(rec_out([]))
# paskal(1)
#------------------------------------------
#
# 10) Число Фибоначчи
# Напишите рекурсивную функцию fib(n), которая будет принимать положительное целое число n и
# возвращать n-ое число Фибоначчи. Числа Фибоначчи — это серия чисел, которая начинается с 0 и 1.
# Каждое последующее число будет являться суммой двух предыдущих чисел.
#0, 1, 1, 2, 3, 5, 8, 13, 21

# arr = [0,1]
# def fib(n):
#     global arr
#     if n < 3:
#         return arr[-1]
#     arr.append(arr[-2] + arr[-1])
#     n -= 1
#     return fib(n)
# print(fib(6))
# print(arr)
#-----------------------
# Менее выполнимые задания
#
# 11) Генерация перестановок. Напишите рекурсивную функцию permutations(list, length), которая
# будет принимать список с его элементами и целочисленную длину, и возвращать все возможные
# перестановки относительно длины внутри списка.

# permutations([1,2,3], 2)
#
# # [(1,2), (1,3), (2,3), (2,1), (3,1), (3,2)]
#
# permutations([1,2,3,4], 2)
#
# # [(1,2), (1,3), (1,4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)]

# arr = []
# def permutations(list, length):
#     global arr
#
#
# permutations([1,2,3], 2)
#-------
# # [(1,2,3), (2,1,3), (2,3,1), (3,2,1), (3,1,2), (1,3,2)]
# # [(1,2), (1,3), (1,4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)]
# arr = [1,2,3,4]
# arr_test = [arr[i] for i in range(2)]
# print(arr_test)
#[1,2,3,4]
#[2,1,3,4]
#[2,3,1,4]
#[2,3,4,1]

# arr_2 = []
# for i in arr:
#     num = 2
#     arr_copy = arr.copy()
#
#     for j in range(len(arr_copy)):
#         res = tuple(arr_copy[j:][item] for item in range(3))
#         arr_2.append(res)
#         arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
#         print(f'jjj {arr_copy}')
#         print(res)
#         print()
#     break
#     #     # arr_2.append(arr_copy) if arr_copy not in arr_2 else ...
#     #     arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
#     #     print(arr_copy)
#     #     arr_2.append(arr_copy)
# print(arr_2)

#     while
#     for j in arr[arr.index(i) + 1:]:
#         arr_2.append((i, j))
#         arr_2.append((j, i))
#
# print(sorted(arr_2, key=lambda x: x[0]))
#-------
# # [(1,2), (1,3), (2,3), (2,1), (3,1), (3,2)]
# def permutations(list, length):
#
# permutations([1,2,3], 2)
#--------------------

# permutations([1,2,3], 2)
#
# # [(1,2), (1,3), (2,3), (2,1), (3,1), (3,2)]
#
# permutations([1,2,3,4], 2)
#
# # [(1,2), (1,3), (1,4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3)]



# [1, 2, 3]
# [2, 1, 3]
# [3, 2, 1]
# [1, 3, 2]
# [2, 3, 1]
# [3, 1, 2]

from itertools import permutations
from random import shuffle

from itertools import zip_longest
from collections import Counter
print(Counter([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]))

# lst_1 = [1,2,3,4,5]
# lst_2 = [6,7,8,9]
# print(list(zip_longest(lst_1, lst_2)))
# print()
# arr = [1,2,3]
#
#
# def factorial(n):
#     if n == 1:
#         return n
#     return n * factorial(n - 1)
#
# f = factorial(len(arr))
# print(f)
# result = []
# VAR = 0
# #while len(result) <= 6 and len(result) == 0 or  [result.count(i) for i in result].count(1) == len(result):
# while len(result) < f:
#     VAR += 1
#     random.shuffle(arr)
#     if (arr[0], arr[1]) not in result:
#         result.append((arr[0], arr[1]))
#     else:
#         continue
#
# print(VAR)
#

# # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]



# #
# # n = 2
#
# #
# # print(factorial(len(arr)))









# def outer():
#     x = 1
#
#     def inner(mul_in):
#         nonlocal x
#         x *= mul_in
#         print(x)
#
#     return inner
#
# f = outer()
# print(f)
#
# for i in range(1, 6):
#     f(i)
#
#
# def factorial(n):
#     if n == 1:
#         return n
#     return n * factorial(n - 1)
#
# print(factorial(5))









# def RecurCombo(array, num):
#     if num == 0:
#         return [[]] # if length for combination is 0
#     l =[] # list to printed in result
#     # Using for loop to implement recursive approach
#     for j in range(0, len(array)):
#         emptyArray = array[j] # define an empty array to print list of sets
#         recurList = array[j + 1:]
#         # Recursion method on list defined in function
#         for x in RecurCombo(recurList, num-1):
#             l.append([emptyArray]+x) # appending list
#     return l # list as result of recursion
# if __name__=="__main__":
#     # Taking an input string from user
#     inputArray = input("Enter an input string to find combinations: ")
#     # Printing different combinations as result in output
#     print("All possible combinations of three letter sets from the string given by you is: ")
#     print(RecurCombo([a for a in inputArray], 3))

# Combinations([1,2,3], 2)
#
# # [(1,2), (1,3), (2,3)]
#
# permutations([1,2,3,4], 2
#
# # [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
# print(f'--------------')
# arr = [1, 2, 3]
#
# def foo(lst, length):
#     if length == 0:
#         return [[]]
#
#     small_lst = foo(lst[1:], length - 1)
#     result = []
#     for i in range(len(lst)):
#
#         for j in small_lst:
#             # if j != []:
#             #     if i > lst.index(j):
#             print(f'ffadf {[lst[i]] + j}')
#             print()
#
#             result.append([lst[i]] + j) if [lst[i]] != j else ...
#
#             print(result)
#             # else:
#             #     result.append([lst[i]] + j)
#
#     print(result)
#     return result
# #
#
# foo([1,2,3,4], 3)



import random
# arr = [2, 3, 2, 1, 4, 7, 4, 7, 1, 10, 2, 7, 10, 5, 4, 6, 3, 7, 4, 5, 8, 10, 3, 9, 6, 5, 7, 1, 8, 8]
#[2, 3, 2, 1, 4, 7, 4, 7, 1, 10, 2, 6, 10, 5, 4, 6, 3, 7, 4, 5, 8, 10, 3, 9, 6, 5, 7, 1, 8, 8]
#[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 10, 10, 10]
#через сортировку
# arr_sort = sorted(arr)
# result_lst = []
# temp = []
# for i in range(len(arr_sort)):
#     if not len(temp):
#         temp=[arr_sort[i]]
#         continue
#
#     if arr_sort[i] == temp[-1]:
#         temp.append(arr_sort[i])
#     else:
#         result_lst.append(temp)
#         temp=[arr_sort[i]]
# print(result_lst)

#не через сортировку
# print()
# print('--------')
# result_lst = []
# temp = []
# idx = 0
# while len(arr) > 0:
#     if idx == len(arr) - 1:
#         result_lst.append(temp)
#         result_lst = sorted(result_lst, key=lambda el: el[0])
#         temp, idx = [], 0
#
#     if len(temp) == 0:
#         temp.append(arr.pop(idx))
#         continue
#
#     if arr[idx] == temp[-1]:
#         temp.append(arr.pop(idx))
#     else:
#         idx += 1
#
#
# print(result_lst)
















# Напишите рекурсивную функцию, которая будет принимать id человека
# и находить всех его друзей, друзей их друзей и так далее.
#
# friends(1) # [1,2,3,4]
# friends(2) # [1,2,3,4]
# friends(3) # [1,2,3,4]
# friends(4) # [1,2,3,4]
#
# friends(5) # [5,6,7]
# friends(6) # [5,6,7]
# friends(7) # [5,6,7]
# g = {
# 1: [2,3], # 1 is friends with 2 and 3
# 2: [1], # 2 is friends with 1
# 3: [1,4], # 3 is friends with 1 and 4
# 4: [3], # etc
# 5: [6, 7],
# 6: [5, 7],
# 7: [6],
# 8: [1,2,3,4,5,6,7]
# }
#
# # def friends(n):
# #
# #
# #
# #
# # friends(5)
#
# lst = []
# def friends(n):
#     if isinstance(g[n], list):
#         for i in g[n]:
#             if i not in lst:
#                 lst.append(i)
#                 friends(i)
#             elif i in lst:
#                 continue
#             else:
#                 return
#
# friends(8)
# print(sorted(lst))







maze = [
  'S----',
  '##---',
  '---##',
  '----X'
]

# s означает стартовую позицию (откуда игрок начинает);
# x означает финиш (цель прохождения лабиринта);
# – означает свободный путь, по которому может осуществлять движение игрок;
# # означает стену, через которую игрок не может пройти.
# Некоторые правила:
# Игрок может двигаться только на 1 шаг за один раз;
# Игрок может двигаться только в 4 направлениях: вверх, вниз, влево, вправо.
# Лабиринт проходим, если игрок может пройти до x из s.
# Напишите рекурсивную функцию, которая будет принимать
# лабиринт и возвращать «True», если он проходим, и «False» в любом другом случае.
#
def lab(maze_arg):
    if len(maze_arg) == 1:
        print(maze_arg)
        return f'буква {maze_arg}'

    for i in maze_arg:
        if isinstance(i, str):
            lab(list(i))

lab(maze)