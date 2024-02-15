import string
from collections import OrderedDict
from timeit import timeit as time_method
from timeit import default_timer
"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

lets = [let for let in string.ascii_uppercase]
def d():
    d_1 = dict()
    key, vol = 0, 0
    for _ in range(5):
        d_1.setdefault(lets[key], vol)
        key, vol = key + 1, vol + 1


def o_d():
    d_2 = OrderedDict()
    key2, vol2 = 0, 0
    for _ in range(5):
        d_2.setdefault(lets[key2], vol2)
        key2, vol2 = key2 + 1, vol2 + 1


t1 = (time_method('d()', 'from __main__ import d', default_timer, number=10, globals=globals()) * 1000000).__round__(3)
t2 = (time_method('o_d()', 'from __main__ import o_d', default_timer, number=10, globals=globals()) * 1000000).__round__(3)

#при малом количестве операций быстрее ordered dict при большом - обычный dict
print(t1)
print(t2)

