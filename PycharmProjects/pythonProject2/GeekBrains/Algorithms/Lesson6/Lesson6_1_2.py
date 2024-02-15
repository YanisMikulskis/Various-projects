from memory_profiler import profile, memory_usage
import numpy as np
from collections import namedtuple, Counter
from timeit import default_timer
import string
import random
from pprint import pprint
from pympler import asizeof as AS
import sys

# Задание 1.

"""
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько вариантов решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
print('################################################################################################')


def deco(func):
    def wrapper(*args):
        m1, t1 = memory_usage(), default_timer()
        result = func(*args)
        m2, t2 = memory_usage(), default_timer()
        mem_diff = m2[0] - m1[0]
        print(f'Памяти при работе функции {func.__name__} занято {mem_diff} MiB\n{t2 - t1} времени')
        return result

    return wrapper


@deco
def classic_way():
    profits_1, qua_comp = [], 10000
    for i in range(qua_comp):  # <- увеличено число компаний для большего взаимодействия с памятью
        name = ''
        for i in range(random.randint(1, 4)):
            name += random.choice(string.ascii_uppercase)
        moneys = [str(random.randint(1, 9999)) for _ in range(4)]
        profits_1.append([name, *moneys])
    cash = [list(map(int, i[1:])) for i in profits_1]
    names_collection = [''.join([random.choice(string.ascii_uppercase) for _ in
                                 range(random.randint(1, 4))]) for i in range(qua_comp)]
    money_collection = [sum([random.randint(1, 9999) for i in range(4)]) for j in range(qua_comp)]
    tuple_comp = [namedtuple('companies', 'name, money') for i in range(qua_comp)]
    profits_1 = [tuple_comp[i](name=names_collection[i], money=money_collection[i]) for i in range(qua_comp)]

    while True:
        profits_year = sum([sum(data) for data in cash]) / len(cash)
        above_average = ', '.join([name[0] for name in profits_1 if name[1] > profits_year])
        less_than_average = ', '.join([name[0] for name in profits_1 if name[1] < profits_year])
        print(f'\nСредняя годовая прибыль всех предприятий: {profits_year.__round__(2)}\n'
              f'Предприятия, с прибылью выше среднего значения: {above_average}\n'
              f'Предприятия, с прибылью ниже среднего значения: {less_than_average}')
        del profits_year, above_average, less_than_average
        break


classic_way()

@deco
def numpy_way():
    qua_comp, names = 10000, string.ascii_uppercase
    # # # #################---NUMPY-----####################
    make_name_company = lambda: ''.join(random.choice(names) for _ in range(random.randint(1, 4)))
    make_company = lambda: [make_name_company(), *[random.randint(1, 9999) for _ in range(4)]]

    comp_money = np.array([make_company() for _ in range(qua_comp)])
    print(f'jjjj {comp_money}')
    only_money = np.array([list(map(int, i[1:])) for i in comp_money])

    year = np.mean([sum(data) for data in only_money])

    above_average = ', '.join(np.array([comp_money[np.where(only_money == data)][0] for data in only_money
                                       if sum(data) > year]))
    less_than_average = ', '.join(np.array([comp_money[np.where(only_money == data)][0] for data in only_money
                                           if sum(data) < year]))

    print(f'Средняя годовая прибыль всех предприятий: {year}\n'
          f'Предприятия, с прибылью выше среднего значения: {above_average}\n'
          f'Предприятия, с прибылью ниже среднего значения: {less_than_average}')
    del comp_money, only_money, year, above_average, less_than_average
    # for data in only_money:
    #     idx = np.where(only_money == data)
    #     if sum(data) > year:
    #         qwe.append(comp_money[idx][0])
    #     else:
    #         qwe2.append(comp_money[idx][0])
    #
    # print(np.sum(comp_money[1:]))


numpy_way()


# Задание 1 из 5 урока (collections). Была использована библиотека numPy и ее механики. В конце работы функции,
# после получения нужной информации были удалены все ссылки. Место занимаемое уменьшилось примерно в 10 раз. Было 58
# MiB, стало 6. Проверка памяти выполнена с помоющью декоратора @deco
@deco
# Памяти занято 9.578125 MiB
# 0.18443329102592543 времени
def double_recursion():
    quantity_2, names = 10000, string.ascii_uppercase
    sys.setrecursionlimit(quantity_2 * 2)
    profits_2 = []
    for _ in range(quantity_2):
        name_2 = ''.join([random.choice(names) for i in range(random.randint(1, 4))])
        mon_2 = [str(random.randint(1, 9999)) for _ in range(4)]
        profits_2.append([name_2, mon_2])

    def companies(arg_data, idx, result):
        idx += 1

        if idx == len(arg_data):
            medium = (sum(list(map(lambda x: x[1], result))) / len(arg_data)).__round__(3)

            min_profit = list(map(lambda x: x[0] if x[1] < medium else ..., result))
            max_profit = list(map(lambda x: x[0] if x[1] > medium else ..., result))

            deliverance_ellipsis = lambda lst: [el for el in lst if el is not Ellipsis]
            max_profit = ', '.join(deliverance_ellipsis(max_profit))
            min_profit = ', '.join(deliverance_ellipsis(min_profit))

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


double_recursion()
