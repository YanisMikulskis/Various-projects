"""Задание 1"""
import random

""" ЗАДАНИЕ 1
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""
# РЕШЕНИЕ ЧЕРЕЗ ЦИКЛ
# operation_list = ['+', '-', '*', '/', '0']
# while True:
#     operation = input('Введите операцию (+, -, *, / или 0 для выхода: ')
#     if operation in operation_list:
#         if operation == '0':
#             print(f'выход из программы')
#             break
#         else:
#             number_1 = int(input('Введите первое число: '))
#             number_2 = int(input('Введите второе число: '))
#             match operation:
#                 case '+': print(int.__add__(number_1, number_2))
#                 case '-': print(int.__sub__(number_1, number_2))
#                 case '*': print(int.__mul__(number_1, number_2))
#                 case '/': print(int.__truediv__(number_1, number_2).__round__(2))
#     else:
#         continue
# # РЕШЕНИЕ ЧЕРЕЗ рекурсию
# operation_list = ['+', '-', '*', '/', '0']
# def calc():
#     operation = input('Введите операцию (+, -, *, / или 0 для выхода: ')
#     if operation == '0':
#         exit(f'Выход из рекурсии')
#     if operation in operation_list:
#         try:
#             number_1 = int(input('Введите первое число: '))
#             number_2 = int(input('Введите второе число: '))
#         except ValueError:
#             print(f'Вы ввели не число! Попробуйте снова')
#             return calc()
#         if number_2:
#             match operation:
#                 case '+': print(f'Ваш результат {number_1 + number_2}')
#                 case '-': print(f'Ваш результат {number_1 - number_2}')
#                 case '*': print(f'Ваш результат {number_1 * number_2}')
#                 case '/': print(f'Ваш результат {round(number_1 / number_2, 2)}')
#         else:
#             print(f'Ноль не может быть делителем!')
#         return calc()
#     else:
#         print(f'Вы ввели неверный знак! Попробуйте снова')
#         return calc()
# calc()
# Задание 2
""" Задание 2 """
"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
# РЕШЕНИЕ ЧЕРЕЗ ЦИКЛ
# number = int(input(f'Ведите натуральное число '))
# even_numbers, not_even_numbers = [],[]
# while number > 10:
#     remainder, number = number % 10, number // 10
#     if number < 10:
#         even_numbers.append(number) if number % 2 == 0 else not_even_numbers.append(number)
#     even_numbers.append(remainder) if remainder % 2 == 0 else not_even_numbers.append(remainder)
# print(f'Количество четных и нечетных цифр в числе равно: {(len(even_numbers), len(not_even_numbers))}')
# РЕШЕНИЕ ЧЕРЕЗ РЕКУРСИЮ
# number = int(input(f'Ведите натуральное число '))
# def EVEN(num, rem, even, not_even):
#     if not num:
#         return f'Количество четных и нечетных цифр в числе равно: ' \
#                f'{len(even), len(not_even)}\n' \
#                f'{sorted(even)}   {sorted(not_even)}'
#     if rem is not None:
#         even.append(rem) if rem % 2 == 0 else not_even.append(rem)
#         if num < 10:
#             even.append(num) if num % 2 == 0 else not_even.append(num)
#     return EVEN(num // 10, num % 10, even, not_even)
# print(EVEN(number, None, [], []))
# Задание 3
""" Задание 3 """
"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""
# Решение через цикл
# num = int(input('введите число которое надо перевернуть '))
# reverse_number = []
# while num >= 10:
#     rem, num = num % 10, num // 10
#     reverse_number.append(rem)
#     reverse_number.append(num) if num < 10 else ...
# print(''.join(list(map(str, reverse_number))))
# Решение через рекурсию
# num = int(input('введите число которое надо перевернуть '))
#
# def reverse_req(number, revs):
#     if number == 0:
#         return ''.join(map(str, revs))
#     number, rem = number // 10, number % 10
#     revs.append(rem)
#     return reverse_req(number, revs)
#
# print(f'Перевернутое число: {reverse_req(num, [])}')
""" Задание 4 """
"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтись без создания массива!
"""
# решение через лямбду и list compr
# n = int(input(f'Введите количество элементов: '))
# rew = [1/2**i for i in range(10)]
# rew_new = list(map(lambda x: x*-1 if rew.index(x)%2 != 0 else x, rew[:n]))
# print(sum(rew_new))
# #решение через рекурсию первым способом
# def ADD(item):
#     result = 1/2**item if item%2==0 else -1/2**item
#     if item == 0:
#         return result
#     return result + ADD(item - 1)
# print(ADD(n-1)) #вычитаем единичку, так как у нас рекурсия приходит к нулевой степени (item = 0)
# # и дает единицу в i, которая участвует в сумме (см задание)
# #решение через рекурсию вторым способом
# def ADD(item, result):
#     result = abs(result)/2 if item%2==0 else abs(result)/-2
#     if item == 0:
#         return result
#     return result + ADD(item - 1, result)
# print(ADD(n-1, 2))
""" Задание 5 """
# """
# Задание 5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
#
# Пример:
# 32 -   33 - ! 34 - " 35 - # 36 - $ 37 - % 38 - & 39 - ' 40 - ( 41 - )
# 42 - * 43 - + 44 - , 45 - - 46 - . 47 - / 48 - 0 49 - 1 50 - 2 51 - 3
# 52 - 4 53 - 5 54 - 6 55 - 7 56 - 8 57 - 9 58 - : 59 - ; 60 - < 61 - =
# 62 - > 63 - ? 64 - @ 65 - A 66 - B 67 - C 68 - D 69 - E 70 - F 71 - G
# 72 - H 73 - I 74 - J 75 - K 76 - L 77 - M 78 - N 79 - O 80 - P 81 - Q
# 82 - R 83 - S 84 - T 85 - U 86 - V 87 - W 88 - X 89 - Y 90 - Z 91 - [
# 92 - \ 93 - ] 94 - ^ 95 - _ 96 - ` 97 - a 98 - b 99 - c 100 - d 101 - e
# 102 - f 103 - g 104 - h 105 - i 106 - j 107 - k 108 - l 109 - m 110 - n 111 - o
# 112 - p 113 - q 114 - r 115 - s 116 - t 117 - u 118 - v 119 - w 120 - x 121 - y
# 122 - z 123 - { 124 - | 125 - } 126 - ~ 127 - 
#
# Решите через рекурсию. В задании нельзя применять циклы.
#
# Допускается исп-е встроенных ф-ций
# """
# import itertools
# #решение через цикл
# # arr = [[ord(chr(i)), '-', chr(i)] for i in range(32, 128)]
# # a_glob, a_down = [], []
# # for i in arr:
# #     if arr.index(i) < len(arr) - len(arr) % 10:
# #         a_down.append(i)
# #         if len(a_down) == 10:
# #             a_glob.append(a_down)
# #             a_down = []
# #     else:
# #         a_down.append(i)
# #         if len(a_down) == len(arr) % 10:
# #             a_glob.append(a_down)
# # for i in a_glob:
# #     print(*list(itertools.chain(*i)))
#
# #решение через рекурсию
# def ASCII_func(number_symbol, string_ascii, step):
#     if number_symbol == 128:
#         return string_ascii
#     couple = f'{ord(chr(number_symbol))} - {chr(number_symbol)} '
#     string_ascii = string_ascii + couple + '\n' if step is not None and step % 10 == 0 else string_ascii + couple
#     number_symbol += 1
#     step += 1
#     return ASCII_func(number_symbol, string_ascii, step)
# print(ASCII_func(32, '', 1))
""" Задание 6 """
# """
# Задание 6.	В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
#
# Решите через рекурсию. В задании нельзя применять циклы.
# """
# import random
#решение через цикл
# step = 10
# number = random.randint(1, 100)
# while step >= 0:
#     user_data = int(input('введите '))
#     if user_data == number or step == 0:
#         if not step:
#             print(f'попыток больше нет! это число {number}')
#             break
#         print(f'Число угадано! {number}')
#         break
#     print(f'Загаданное число больше! Осталось попыток: {step}') if user_data < number \
# else print(f'Число меньше!осталось попыток: {step}')
#     step -= 1

#решение через рекурсию
# words = ['попыток','попытки', 'попытка']
# def GAME_number(number, step):
#     user_number = int(input('Введите число: '))
#     step -= 1
#     if user_number == number or step == 0:
#         if not step:
#             return f'Попыток больше нет! это число {number}'
#         return f'Число угадано! это {number}'
#     print(f'Загаданное число БОЛЬШЕ! '
#           f'Осталось {step} {words[0] if step >= 5 else words[1] if step != 1 else words[2]}') \
#         if user_number < number \
#         else print(f'Загаданное число МЕНЬШЕ! '
#                    f'Осталось {step} {words[0] if step >= 5 else words[1] if step != 1 else words[2]}')
#     return GAME_number(number, step)
# print(GAME_number(random.randint(0, 100), 10))
""" Задание 7 """
"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""
# n = 5
# var = 0
# def maths_ind(number):
#     if number == 0:
#         return number
#     return number + maths_ind(number - 1)
# print(True) if maths_ind(n) == n*(n+1)/2 else ...
#
#
# print(True) if sum([i for i in range(1, n + 1)]) == n*(n+1)/2 else Ellipsis
#
#
# while n != 0:
#     var += n
#     n -= 1
#
# print(var)

