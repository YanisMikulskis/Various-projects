from file import *

# import re
# date = '02.11.2013'
#
#
# numbers_date = date.split('.')
# numbers = {
#     '01': 'первое',
#     '02': 'второе',
#     '03': 'третье'
# }
# print(numbers.get('02'))
# months = {
#     '10': 'октября',
#     '11': 'ноября',
#     '12': 'декабря'
# }
# result = f'{numbers.get(numbers_date[0])} ' \
#          f'{months.get(numbers_date[1])} ' \
#          f'{numbers_date[2]} года'
# print(result)
#дан произвольный список длиной 100. все четные числа в нем возвести в квадрат, а к нечетным прибавить 10.
#решить задачу минимум двумя способами
import random as rnd
# arr = [86, 53, 94, 0, 21, 10, 65, 52, 49, 31, 9, 7, 99, 44, 80, 55, 77, 68, 89, 88, 49, 85, 38, 66, 52, 4, 98, 25, 68, 12, 52, 78, 32, 63, 60, 48, 51, 98, 7, 79, 71, 10, 15, 12, 49, 25, 73, 15, 81, 23, 66, 88, 42, 69, 63, 5, 36, 71, 76, 14, 57, 42, 37, 0, 9, 2, 24, 60, 50, 74, 0, 89, 9, 16, 99, 60, 66, 76, 37, 78, 99, 94, 93, 50, 97, 78, 47, 92, 44, 17, 47, 9, 75, 10, 99, 36, 13, 30, 98, 80]
# #1
# arr_new = list(map(lambda x: x ** 2 if not x % 2 else x + 10, arr))
# print(arr_new)
# #2
# arr_new_2 = []
# for i in arr:
#     if i % 2 == 0:
#         arr_new_2.append(i ** 2)
#     else:
#         arr_new_2.append(i + 10)
# print(arr_new_2)

# def foo():
#     def foo2():
#         foo()
#         print(1)
#     foo2()
# foo()

import time

# var = 0
# inc = 1
# while 1:
#     time.sleep(0.5)
#     print(var)
#     var += inc
#     if var == 10 or not var:
#         inc *= -1

# var2 = 0
# result = 0
# inc2 = 1
#
# arr = list(range(11))
# #
# for i in range(10):
#     print(i)
# while 1:
#     for i in arr:
#         print(i)
#         time.sleep(0.5)
#
#         if i == 10 or not i:
#             arr.reverse()
car = Car()
print(car.color)
car.met()