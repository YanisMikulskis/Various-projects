from collections import deque
from timeit import timeit as time_method

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

# def ap_left():
#     experimental_var = 0.1
#     for i in range(10):
#         easy_dq.appendleft(experimental_var)
# def ins_lst():
#     experimental_var = 0.1
#     for i in range(10):
#         easy_list.insert(0, experimental_var)
#
#
# print((time_method('ap_left()', 'from __main__ import ap_left', number=1, globals=globals()) * 1000000).__round__(3))
# print((time_method('ins_lst()', 'from __main__ import ins_lst', number=1, globals=globals()) * 1000000).__round__(3))
#
# def p_left_deq():
#     for i in range(10):
#         easy_dq.popleft()
#
# def p_list():
#     for i in range(10):
#         easy_list.remove(easy_list[0])
#
# print(easy_dq)
# p_left_deq()
# print(easy_dq)
#
# print(easy_list)
# p_list()
# print(easy_list)
# print((time_method('p_left_deq()', 'from __main__ import p_left_deq', number=1, globals=globals()) * 1000000).__round__(3))
# print((time_method('p_list()', 'from __main__ import p_list', number=1, globals=globals()) * 1000000).__round__(3))
#операция со списком работает дольше
# def ex_left_deq():
#     for i in range(10):
#         easy_dq.extendleft([1,2,3])
#
# def ex_list():
#     easy_list.reverse()
#     for i in range(10):
#         easy_list.extend([1,2,3])
#     easy_list.reverse()
# print((time_method('ex_left_deq()', 'from __main__ import ex_left_deq', number=10, globals=globals()) * 1000000).__round__(3))
# print((time_method('ex_list()', 'from __main__ import ex_list', number=10, globals=globals()) * 1000000).__round__(3))
#примерно одинаковое время

def Foo_1():
    return easy_dq[1]
def Foo_2():
    return easy_list[1]


print((time_method('Foo_1()', 'from __main__ import Foo_1', number=10, globals=globals()) * 1000000).__round__(3))
print((time_method('Foo_2()', 'from __main__ import Foo_2', number=10, globals=globals()) * 1000000).__round__(3))
#список быстрее