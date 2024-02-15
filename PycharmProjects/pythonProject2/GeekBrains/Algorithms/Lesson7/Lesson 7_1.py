"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
import random
from timeit import default_timer
# arr = [random.randint(-100, 100) for _ in range(20)]

def deco(func):
    def wrapper(*args):
        t1 = default_timer()
        res = func(*args)
        t2 = default_timer()
        time_diff = t2 - t1
        print(f'время {time_diff}')
        return res
    return wrapper





# arr = [-95, 16, 15, 88, 1, -93, -20, 5, -10, -49, 4, -43, 2, 29, -96, 33, -55, 73, 52, -1]

arr = [random.randint(-100, 100) for _ in range(100)]
var = 0
arr_2 = list(reversed(list(range(100))))

@deco
def bubble_sort(lst):
    elem = 0
    sort_bool = False
    while elem < len(lst) - 1:

        item = -1
        while item > (-len(lst)) + elem:

            if lst[item] > lst[item - 1]:
                sort_bool = True
                lst[item], lst[item - 1] = lst[item - 1], lst[item]
            item -= 1
        if not sort_bool:
            break
        elem += 1


    # elem = 0
    # sort_bool = False
    # while elem < len(lst) - 1:
    #
    #     item = 0
    #     while item < (len(lst) - 1) - elem:
    #         print(lst)
    #         if lst[item] > lst[item + 1]:
    #             sort_bool = True
    #             lst[item], lst[item + 1] = lst[item + 1], lst[item]
    #         item += 1
    #     if not sort_bool:
    #         break
    #
    #     elem += 1

    print(sort_bool)
    print(lst)
bubble_sort(arr_2)