"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from statistics import median
from memory_profiler import memory_usage
from timeit import default_timer
from random import randint as rint
arr2 = [rint(-100, 100) for _ in range(1000)]
print(arr2)
t1 = default_timer()
m1 = memory_usage()[0]
print(median(arr2))
m2 = memory_usage()[0]
t2 = default_timer()
print(f'память {m2 - m1}\n{t2 - t1}')