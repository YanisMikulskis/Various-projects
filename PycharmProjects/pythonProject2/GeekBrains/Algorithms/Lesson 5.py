import string
from collections import namedtuple, defaultdict, deque
import statistics
from string import ascii_uppercase
from timeit import timeit as time_method
from timeit import default_timer

##########################################################################################################
##########################################################################################################
##########################################################################################################
# """
# Задание 1.
#
# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего
#
# Подсказка:
# Для решения задачи обязательно примените коллекцию из модуля collections
# Для лучшего освоения материала можете сделать
# несколько варианто решения этого задания,
# применив несколько коллекций из модуля collections
#
# Пример:
# Введите количество предприятий для расчета прибыли: 2
# Введите название предприятия: Рога
# через пробел введите прибыль данного предприятия
# за каждый квартал(Всего 4 квартала): 235 345634 55 235
#
# Введите название предприятия: Копыта
# через пробел введите прибыль данного предприятия
# за каждый квартал(Всего 4 квартала): 345 34 543 34
#
# Средняя годовая прибыль всех предприятий: 173557.5
# Предприятия, с прибылью выше среднего значения: Рога
# Предприятия, с прибылью ниже среднего значения: Копыта
# """
# print('################################################################################################')
#
# # #1 способ (обычный)
# quantity_1 = int(input('количество предприятий: '))
# profits_1 = []
# for _ in range(quantity_1):
#     name_1 = input('введите название компании: ')
#     mon_1 = input('введите прибыль за кварталы: ').split()
#     profits_1.append([name_1, mon_1])
#
# # profits = [['rog', ['235', '345634', '55', '235']], ['kop', ['345', '34', '543', '34']],
# #            ['lag', ['235', '345634', '55345', '235']]]
# while True:
#     try:
#         profits_1 = list(map(lambda x: [x[0], sum(list(map(int, x[1])))], profits_1))
#     except ValueError:
#         print(f'В одной из сумм предприятий введено не число!')
#         for i in profits_1:
#             for j in i:
#                 if isinstance(j, list):
#                     for item in j:
#                         match item.isdigit():
#                             case False:
#                                 j[j.index(item)] = item.replace(item, '11111')
#     else:
#         profits_year = sum([data[1] for data in profits_1]) / quantity_1
#         above_average = ' '.join([name[0] for name in profits_1 if name[1] > profits_year])
#         less_than_average = ' '.join([name[0] for name in profits_1 if name[1] < profits_year])
#         print(f'Средняя годовая прибыль всех предприятий: {profits_year.__round__(2)}\n'
#               f'Предприятия, с прибылью выше среднего значения: {above_average}\n'
#               f'Предприятия, с прибылью ниже среднего значения: {less_than_average}')
#         break
#
# print('################################################################################################')
#
# # 2 двойная Рекурсия
quantity_2 = int(input('Количество: '))
profits_2 = []
for _ in range(quantity_2):
    name_2 = input('введите название компании: ')
    mon_2 = input('введите прибыль за кварталы: ').split()
    profits_2.append([name_2, mon_2])

print(profits_2)
def companies(arg_data, idx, result):
    idx += 1

    if idx == len(arg_data):
        medium = (sum(list(map(lambda x: x[1], result))) / len(arg_data)).__round__(3)
        min_profit = []
        max_profit = list(map(lambda x: x[0] if x[1] > medium else min_profit.append(x[0]), result))
        max_profit.pop(max_profit.index(None))
        max_profit, min_profit = ' '.join(max_profit), ' '.join(min_profit)
        return f'Средняя сумма {medium}\n' \
               f'Компании с большим оборотом {max_profit}\n' \
               f'Компании с меньшим оборотом {min_profit}'

    def companies_2(arg_data_2, idx_2):
        idx_2 += 1
        if idx_2 == len(arg_data_2):
            return
        element_now = arg_data_2[idx_2]
        if isinstance(element_now, list):
            all_money = [arg_data_2[0], sum(list(map(lambda x: int(x) if x.isdigit() else ..., element_now)))]
            result.append(all_money)
        return companies_2(arg_data_2, idx_2)

    companies_2(arg_data[idx], -1)
    return companies(arg_data, idx, result)


print(companies(profits_2, -1, []))
#
# print('################################################################################################')
# #
# # 3 Через collections
#
# quantity_3 = int(input('Количество: '))
#
# profits_3 = []
# for _ in range(quantity_3):
#     name_3 = input('введите название компании: ')
#     mon_3 = input('введите прибыль за кварталы: ').split()
#     profit_sample = namedtuple(f'{name_3}', 'qua_1 qua_2 qua_3 qua_4')
#     profit_tuple = profit_sample(
#         qua_1=mon_3[0],
#         qua_2=mon_3[1],
#         qua_3=mon_3[2],
#         qua_4=mon_3[3]
#     )
#     general_profit_integer = sum(list(map(lambda x: int(x), profit_tuple)))
#     profits_3.append([profit_sample.__name__, general_profit_integer])
#
# medium = statistics.fmean(data[1] for data in profits_3)
# max_profit = [name[0] for name in profits_3 if name[1] > medium]
# min_profit = [name[0] for name in profits_3 if name[1] < medium]
#
# print(medium.__round__(3))
# print('Лучшие компании', *max_profit)
# print('Худшие компании', *min_profit)
##########################################################################################################
##########################################################################################################
##########################################################################################################
# """
# Задание 2.
#
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#
# Подсказка:
# Попытайтесь решить это задание в двух вариантах
# 1) через collections
#
# defaultdict(list)
# int(, 16)
# reduce
#
# 2) через ООП
#
# вспомните про перегрузку методов
#
# __mul__
# __add__
# """


# 1 через collections

# def main_1():
#     numbers = [num for num in range(10, 16)]
#     letters = namedtuple('letters', 'A B C D E F')(*numbers)
#
#     def decryption(num_16):
#         num_new = list(map(lambda x: int(x) if x.isdigit() else letters._asdict()[x], num_16))
#         print(f'ИСКОМЫЙ СПИСОК {num_new}')
#
#         def decryption_rec(lst, idx):
#             if idx == len(lst):
#                 return lst
#             lst[idx] = lst[idx] * (16 ** idx)
#             idx += 1
#             return decryption_rec(lst, idx)
#
#         result = decryption_rec(list(reversed(num_new)), 0)
#         return sum(result)
#
#     def cryption(num_10, lst):
#         if not num_10:
#             lst = list(map(str, lst))
#             return lst
#         remainder, num_10 = num_10 % 16, num_10 // 16
#         remainder = letters._fields[letters.index(remainder)] if remainder in letters else remainder
#         lst.insert(0, remainder)
#         return cryption(num_10, lst)
#
#     # --------------ввод данных
#     # 3313
#     # ['C', 'F', '1']
#     # ['7', 'C', '9', 'F', 'E']
#     # num_1 = input('1 число ')#3E8'
#     num_1 = 'A2'
#     arr_1 = [_ for _ in num_1]
#
#     # num_2 = input('2 число ')#5A
#     num_2 = 'C4F'
#     arr_2 = [_ for _ in num_2]
#
#     def_d = defaultdict(list)
#     def_d['1 NUM'] = arr_1
#     def_d['2 NUM'] = arr_2
#
#     result_add = 0
#     result_mul = 1
#     for i in def_d.values():
#         result_add += decryption(i)
#         result_mul *= decryption(i)
#
#     print(f'Суммa чисел в 10x системе = {result_add}')
#     print(f'Сумма в 16х системе = {cryption(result_add, [])}')
#     print(f'Произведение двух чисел в 16х системе = {cryption(result_mul, [])}')
#
#
# main_1()
#
# # 2 через перегрузку
# # def main_2():
# #     letters_crypt = {let: number for let, number in zip(string.ascii_uppercase[:6], [_ for _ in range(10, 17)])}
# #
# #     class NUMBER16:  # сделать 2 атрибута из чисел???
# #         def __init__(self, number_1, number_2):
# #             self.decrypt_number_1 = NUMBER16.decryption(number_1)
# #             self.decrypt_number_2 = NUMBER16.decryption(number_2)
# #
# #         @staticmethod
# #         def decryption(number_static_16):# сюда приходит 16-ричное число и мы его ДЕшифруем
# #             print(f'flag {number_static_16}')
# #             def exam(lst, idx):
# #                 if idx == len(lst):
# #                     return lst
# #                 lst[idx] = letters_crypt[lst[idx]] if lst[idx] in letters_crypt else int(lst[idx])
# #                 idx += 1
# #                 print(f'flag2 {lst}')
# #                 return exam(lst, idx)
# #
# #             result_list = list(reversed(exam(number_static_16, 0)))
# #             result_number = sum(list(map(lambda x: x * (16 ** result_list.index(x)), result_list)))
# #             print(result_number)
# #             return result_number
# #
# #         @staticmethod
# #         def cryption(number_static_10):  # сюда приходит 10-тичное число и мы его ШИФРУЕМ
# #
# #             def recursion_cryption(number, lst):
# #                 if not number:
# #                     lst = list(map(str,lst))
# #                     return lst
# #                 remainder, number = number % 16, number // 16
# #                 if remainder in letters_crypt.values():
# #                     remainder = list(letters_crypt.keys())[list(letters_crypt.values()).index(remainder)]
# #                 lst.insert(0, remainder)
# #                 return recursion_cryption(number, lst)
# #
# #             return recursion_cryption(number_static_10, [])
# #
# #         def __add__(self):
# #             return NUMBER16.cryption(self.decrypt_number_1 + self.decrypt_number_2)
# #
# #         def __mul__(self):
# #             return NUMBER16.cryption(self.decrypt_number_1 * self.decrypt_number_2)
# #     # number_1 = ' '.join(input(f'1 число ')).split() #'A', '2'
# #     # number_2 = ' '.join(input(f'2 число ')).split() # 'C', '4', 'F'
# #
# #     num = NUMBER16(['A', '2'], ['C', '4', 'F'])
# #     print(f'сумма введенных чисел: {num.__add__()}')
# #     print(f'произведение введенных числе: {num.__mul__()}')
# #
# # #как это работает?1. Вводим два числа в 16-х системе. 2. Закидываем их в атрибуты 3. внутри класса они переводятся
# # #в обычную 10х систему (функция decryption (функция, а не метод! так как мы применили декоратор @staticmethod, который
# # #освобождает нас от постоянного ввода атрибутов при обращении к этой функции)4. результаты этой функции (для каждого
# # #из двух числе суммируются и умножаются. Потом эта сумма прилетает в функцию шифрования, которая переводит
# # # назад в 16х систему, а после нее и произведение. Получаем результат сложения и унможения в 16х системе.
# #
# # main_2()
##########################################################################################################
##########################################################################################################
##########################################################################################################
"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует действительности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

easy_list = [i ** 2 for i in range(200)]
easy_dq = deque([i ** 2 for i in range(200)]) # deque([0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

# easy_dq = deque('Hello, World!')
# print(easy_dq)
#1
#list
# def append_op():
#     for i in range(10):
#         easy_list.append(100)
#
# def append_deque():
#     for i in range(10):
#         easy_dq.append(100)






# print((time_method('append_op()', 'from __main__ import append_op', number=100, globals=globals()) * 1000000).__round__(3))
# print((time_method('append_deque()', 'from __main__ import append_deque', number=100, globals=globals()) * 1000000).__round__(3))
#дек срабатывает быстрее, если операций меньше. в противном случае - лист
# def pop_list():
#
#     easy_list.pop()
# def pop_deq():
#     for i in range(2):
#         easy_dq.pop()
#
# print((time_method('pop_list()', 'from __main__ import pop_list', number=100, globals=globals()) * 1000000).__round__(3))
# print(easy_list)
# print((time_method('pop_deq()', 'from __main__ import pop_deq', number=100, globals=globals()) * 1000000).__round__(3))
#при одном запуске
# 1.209
# 0.833
#дек быстрее

# def ex_list():
#     for i in range(5):
#         easy_list.extend([1, 2, 3])
#
#
# def ex_deq():
#     for i in range(5):
#         easy_dq.extend([1, 2, 3])
#
# print((time_method('ex_list()', 'from __main__ import ex_list', number=1, globals=globals()) * 1000000).__round__(3))
# print((time_method('ex_deq()', 'from __main__ import ex_deq', number=1, globals=globals()) * 1000000).__round__(3))
# #если много вызовов - быстрее list.если мало - deq
# #дек срабатывает быстрее, если операций меньше. в противном случае - лист
# print(easy_dq[4])


# 2) сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее