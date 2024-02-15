"""
Задание 1.

Для каждой из трех функций выполнить следующее:

1) для каждого выражения вместо символов !!! укажите сложность.
2) определите сложность алгоритма в целом (Сложность: !!!).

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- Сложность нужно указать только там, где есть !!!
-- Сложности встроенных функций и операций нужно искать
    в таблицах (см. материалы к уроку).
"""

# from random import sample
# ##############################################################################
# def check_1(lst_obj):
#     """Функция должна создать множество из списка.
#
#     Алгоритм 1:
#     Создать множество из списка
#
#     Сложность: O(N) + O(1) = O(N).
#     """
#     lst_to_set = set(lst_obj)  # O(N)
#     return lst_to_set  # !!! O(1)
#
#
# ##############################################################################
# def check_2(lst_obj):
#     """Функция должная вернуть True, если все элементы списка различаются.
#
#     Алгоритм 2:
#     Проходимся по списку и для каждого элемента проверяем,
#     что такой элемент отсутствует
#     в оставшихся справа элементах
#
#     Сложность: O(N^2)
#     """
#     for j in range(len(lst_obj)):          # O(N)
#         if lst_obj[j] in lst_obj[j+1:]:    # O(N) + O(N) = O(N)
#             return False                   # O(1)
#     return True                            # O(1)
#
#
# ##############################################################################
# def check_3(lst_obj):
#     """Функция должная вернуть True, если все элементы списка различаются.
#
#     Алгоритм 3:
#     Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
#     Если присутствуют дубли, они будут находиться рядом.
#
#     Сложность: (O(N) + O(N Log N)) + (O(N) * O(1) + O(1) + O(1)) = O(N Log N) + O(N)=O(N Log N)
#     """
#     lst_copy = list(lst_obj)                 #O(N)
#     lst_copy.sort()                          # O(N Log N)
#     for i in range(len(lst_obj) - 1):        # O(N)
#         if lst_copy[i] == lst_copy[i+1]:     # O(1) ???
#             return False                     # O(1)
#     return True                              # O(1)
#
#
# for j in (50, 500, 1000, 5000, 10000):#O(N)
#     # Из 100000 чисел возьмем 'j' случайно выбранных
#     # Всего 10 тыс. чисел
#     lst = sample(range(-100000, 100000), j) #O(N)
#
#
# #O(N**2)
# print(check_1(lst))
# print(check_2(lst))
# print(check_3(lst))
#-------------------------
# """
# Задание 2.
#
# Реализуйте два алгоритма.
#
# Оба должны обеспечивать поиск минимального значения для списка.
#
# Сложность первого алгоритма должна быть O(n^2) - квадратичная.
#
# Сложность второго алгоритма должна быть O(n) - линейная.
#
#
# Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
# -- нельзя использовать встроенные функции min() и sort()
# -- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
# -- проставьте сложности каждого выражения в двух ваших алгоритмах
# """
# import random
# arr = [5, 7, 8 , 10, 4]
#
#
# def Alg_1(lst, result):
#     for i in lst:
#         if not result:
#             result.append(i)
#         for j in arr[arr.index(i):]:
#             result[0] = j if j < result[0] else result[0]
#     return result[0]
#
# print(Alg_1(arr, []))
#
#
#
#
# def Alg_2(lst, lst_2):
#     for j in lst:
#         lst_2 = lst[0] if not lst_2 else lst_2
#         lst_2 = j if j < lst_2 else lst_2
#     return lst_2
# print(Alg_2(arr, None))
#-------------------------

# """
# Задание 3.
#
# Для этой задачи
# 1) придумайте 2-3 решения (обязательно с различной сложностью)
# 2) оцените сложность каждого выражения в этих решениях в нотации О-большое
# 3) оцените итоговую сложность каждого решения в нотации О-большое
# 3) сделайте вывод, какое решение эффективнее и почему
#
# Сама задача:
# Имеется хранилище с информацией о компаниях: название и годовая прибыль.
# Для реализации хранилища можно применить любой подход,
# который вы придумаете, например, реализовать словарь.
# Реализуйте поиск трех компаний с наибольшей годовой прибылью.
# Выведите результат.
#
# Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
# """
# companies = {
#     'A': 1300,
#     'B': 10,
#     'C': 200000000,
#     'D': 12000,
#     'E': 1,
#     'F': 1201000000
# }
#
# #Решение 1
# def sol_1(arg_dict):
#     ass = [arg_dict.get(k) for k in arg_dict]
#     return '\n'.join(list(map(lambda x: str(x), [ass.pop(ass.index(max(ass))) for _ in range(3)])))
#
# # #Решение 2
# def sol_2(arg_dict):
#     max_2 = []
#     for step in range(3):
#         temporary_list = []
#         for k,v in arg_dict.items():
#             temporary_list.append(v) if not temporary_list else ...
#             temporary_list[0] = v if temporary_list[0] < v else temporary_list[0]
#         arg_dict = {k:v for k,v in arg_dict.items() if v != temporary_list[0]}
#         max_2.append(temporary_list[0])
#     return '\n'.join(list(map(lambda x:str(x), max_2)))
#
# #Решение 3
# def sol_3(arg_dict):
#     max_3, all_values = [],[k[1] for k in arg_dict.items()]
#     for _ in range(3):
#         temporary_var, idx = None, 0
#         for i in all_values:
#             if all_values[idx] < i:
#                 idx = all_values.index(i)
#                 temporary_var = i
#             else:
#                 temporary_var = all_values[idx]
#         max_3.append(temporary_var)
#         all_values.pop(all_values.index(temporary_var))
#     return '\n'.join(list(map(lambda x:str(x), max_3)))
#
# print(f'первый способ:\n{sol_1(companies)}\n')
# print(f'Второй способ\n{sol_2(companies)}\n')
# print(f'Третий способ\n{sol_3(companies)}\n')
#------------------------------------
# """
# Задание 4.
#
# Для этой задачи:
# 1) придумайте 2-3 решения (обязательно с различной сложностью)
# 2) оцените сложность каждого выражения в этих решениях в нотации О-большое
# 3) оцените итоговую сложность каждого решения в нотации О-большое
# 4) сделайте вывод, какое решение эффективнее и почему
#
# Сама задача:
# Пользователи веб-ресурса проходят аутентификацию.
# В системе хранятся логин, пароль и отметка об активации учетной записи.
#
# Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
# При этом его учетка должна быть активирована.
# А если нет, то польз-лю нужно предложить ее пройти.
#
# Приложение должно давать ответы на эти вопросы
#  и быть реализовано в виде функции.
# Для реализации хранилища можно применить любой подход,
# который вы придумаете, например, применить словарь.
#
# Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
# """
# system = {
#     'us1': {'password':111, 'activation': True},
#     'us2': {'password':22, 'activation': True},
#     'us3': {'password':333, 'activation': True},
#     'us4': {'password':44, 'activation': True},
#     'us5': {'password':555, 'activation': False}
# }
#
# #1 способ------------------------------
# def enter_1(arg_sys, log, pas):
#     global x
#     if arg_sys.get(log):
#         dict_values = arg_sys.get(log)
#         for _,_ in dict_values.items():
#             if dict_values['password'] == pas:
#                 if dict_values['activation']:
#                     return 'Вы зашли'
#                 else:
#                     return 'Запись не активна! Активируйте ее'
#             else:
#                 return 'Пароль неверный!'
#     else:
#         return f'пользователь не найден'
# #2 способ-----------------------------
# def enter_2(arg_sys, log, pas):
#     user_names = [name for name in arg_sys.keys()]
#     if log in user_names:
#         user_data = [data for data in arg_sys.get(log).values()]
#         if pas in user_data:
#             if user_data[1]:
#                 return f'Вы вошли!'
#             else:
#                 return 'Активируйте учетную запись!'
#         else:
#             return f'Неправильный пароль!'
#     else:
#         return f'пользователя не существует'
# #3 способ-----------------------------
# def enter_3(arg_sys, log, pas):
#     for k1,v1 in arg_sys.items():
#         if log == k1:
#             temp_arr = []
#             for k2, v2 in v1.items():
#                 temp_arr.append(True) if k2 == 'password' and v2 == pas else ...
#                 temp_arr.append(True) if k2 == 'activation' and v2 else ...
#             if temp_arr.count(True) == len(arg_sys.get(k1)):
#                 return f'Вы вошли третьим способом!'
#             else:
#                 return f'Ошибка! Неправильный пароль или/и учетная запись не активирована!'
# print(enter_1(system, 'us1', 111))
# print(enter_2(system, 'us2', 22))
# print(enter_3(system, 'us1', 111))
############################
############################
############################
############################
# """
# Задание 5. На закрепление навыков работы со стеком
#
# Реализуйте собственный класс-структуру "стопка тарелок".
#
# Мы можем складывать тарелки в стопку и при превышении некоторого значения
# нужно начать складывать тарелки в новую стопку.
#
# Структура должна предусматривать наличие нескольких стопок.
# Создание новой стопки происходит при достижении предыдущим
# стеком порогового значения.
#
# После реализации структуры, проверьте ее работу на различных сценариях.
#
# Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
# --реализуйте по аналогии с примером, рассмотренным на уроке
# --создание нового стопки можно реализовать добавлением нового пустого массива
# в массив стопок (lst = [[], [], [], [],....]).
# """
# import random as rnd
#
# class Plat:
#     def __init__(self):
#         self.all_plats = []
#         self.plats = []
#         self.length = rnd.randint(3, 5)
#     def push_in(self, el):
#         if len(self.plats) < self.length:
#             self.plats.append(el)
#             if len(self.plats) == self.length:
#                 self.plats_copy = self.plats.copy()
#                 #^копия списка, так как при поледующем его очищении(обнуление стека)
#                 #он будет очищаться и в общем списке(all_plats).
#                 #а нам нужно его там оставить
#                 self.all_plats.append(self.plats_copy)
#                 self.plats.clear()
#                 self.length = rnd.randint(3, 5)
#     def view(self):
#         for i in self.all_plats:
#             print(i)
#
#
#
#
# def main():
#     plat = Plat()
#     [plat.push_in('ТАРЕЛКА') for _ in range(30)]
#     plat.view()
# if __name__ == '__main__':
#     main()
############################
############################
############################
############################
# """
# Задание 6. На закрепление навыков работы с очередью
#
# Примечание: в этом задании вспомните ваши знания по работе с ООП
# и опирайтесь на пример урока
#
# Реализуйте класс-структуру "доска задач".
#
# Структура должна предусматривать наличие нескольких очередей задач, например
# 1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
# 2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
# на корректировку решения
# 3) список решенных задач, куда задачи перемещаются из базовой очереди или
# очереди на доработку
#
# После реализации структуры, проверьте ее работу на различных сценариях
#
# Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
# """
# def main():
#     class Queue:
#         def __init__(self):
#             self.task_base = []
#             self.task_revision = []
#             self.task_complete = []
#         def in_task_base(self, task):
#             self.task_base.insert(0, task)
#         def in_task_revision(self):
#             rev_task_base = self.task_base.pop()
#             self.task_revision.insert(0, rev_task_base)
#         def in_task_complete(self):
#             complete_task_base = self.task_base.pop()
#             self.task_complete.insert(0, complete_task_base)
#         def in_task_complete_rev(self):
#             complete_task_rev = self.task_revision.pop()
#             self.task_complete.insert(0, complete_task_rev)
#         def view(self):
#             board = 'Доска пуста'
#             return f'База ВСЕХ задач {self.task_base if len(self.task_base) > 0 else board}\n' \
#                    f'Задачи в доработке {self.task_revision if len(self.task_revision) > 0 else board}\n' \
#                    f'выполненные задачи: {self.task_complete if len(self.task_complete) > 0 else board}'
#     queue = Queue()
#     queue.in_task_base(1)
#     queue.in_task_base(2)
#     queue.in_task_base(3)
#     queue.in_task_base(4)
#     queue.in_task_base(5)
#     queue.in_task_base(6)
#     queue.in_task_revision()
#     queue.in_task_complete()
#     queue.in_task_complete_rev()
#     print(queue.view())
#
# if __name__ == '__main__':
#     main()


"""
Задание 7. На закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром и в таких строках (включающих пробелы)

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""
class Deck:
    def __init__(self):
        self.deck = []
    def view(self):
        return self.deck
    def in_front(self, el):
        self.deck.append(el)
    def in_rear(self, el):
        self.deck.insert(0, el)
    def out_front(self):
        return self.deck.pop()
    def out_rear(self):
        return self.deck.pop(0)
    def size(self):
        return len(self.deck)
# deck = Deck()
# deck.in_front(1)
# deck.in_front(2)
# deck.in_front(3)
# print(deck.view())
# deck.in_rear(1)
# deck.in_rear(2)
# deck.in_rear(3)
# print(deck.view())
# print(f'dddddd {deck.out_front()}')
# deck.out_rear()
# print(deck.view())
# print(deck.size())

def Poly(word):
    deck_word = Deck()
    for i in word:
        deck_word.in_front(i)
    var = True
    while var and deck_word.size() > 1:
        left_let = deck_word.out_rear()
        right_let = deck_word.out_front()
        # if left_let == ' ':
        #     left_let = deck_word.out_rear()

        left_let = deck_word.out_rear() if left_let == ' ' else left_let
        right_let = deck_word.out_rear() if right_let == ' ' else right_let
        if deck_word.size() == 1:
            return f'Слово палиндром'
        elif left_let != right_let:
            print(left_let)
            print(right_let)
            print(deck_word.size())
            print(deck_word.view())
            var = False

    if not var:
        return 'НЕ ПАЛИНДРОМ'








print(Poly('молоко делили ледоколом'))