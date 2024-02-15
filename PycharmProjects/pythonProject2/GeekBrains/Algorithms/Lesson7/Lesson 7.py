""" Алгоритмы сортировки"""
import random
from timeit import timeit as method_timer


#Сортировка выбором

# arr = [-88, 41, -6, -96, 42, 96, 38, -38, 28, 72]
# def selections_sort1(lst):
#     for item in range(len(lst)):
#         var = item
#         for elem in range(item + 1, len(lst)):
#             var = elem if lst[elem] < lst[var] else var
#         lst[item], lst[var] = lst[var], lst[item]
#     return lst
# print(selections_sort1(arr[:]))
# print()
# print()
# #BAD CODE!!!! ниже
#
# arr_2 = arr.copy()
# def selection_sort(lst_obj):
#     for i in range(len(lst_obj)):
#         print(lst_obj)
#         idx_min = i
#         for j in range(i + 1, len(lst_obj)):
#             if lst_obj[j] < lst_obj[idx_min]:
#                 idx_min = j
#         tmp = lst_obj[idx_min]
#         lst_obj[idx_min] = lst_obj[i]
#         lst_obj[i] = tmp
#     return lst_obj
#
# print(selection_sort(arr_2[:]))
#
#
# print(method_timer("selections_sort1(arr[:])", globals=globals(), number=1000))





#Сортировка вставками
# arr = [-88, 41, -6, -96, 42, 96, 38, -38, 28, 72]
# n = 3
# while arr[n] < arr[n - 1] and n:
#     print(arr)
#     arr[n], arr[n - 1] = arr[n - 1], arr[n]
#     print(arr)
#     print()
#     n -= 1
# print(arr)

# def insertion_sort(lst):
#     for el in range(len(lst)):
#         while lst[el] < lst[el - 1] and el:
#             lst[el], lst[el - 1] = lst[el - 1], lst[el]
#             el -= 1
#         print()
#
#     print(lst)
# insertion_sort(arr)



#Сортировка пузырьком

# Какой-то другой способ ниже


# idx_now = 0
# for elem in range(len(arr) - 1):
#     idx_now = 0
#     while 1:
#         if idx_now < len(arr2) - 1 and arr2[idx_now] > arr2[idx_now + 1]:
#             arr2[idx_now], arr2[idx_now + 1] = arr2[idx_now + 1], arr2[idx_now]
#             print(arr2)
#             if arr2[idx_now] < arr2[idx_now + 1]:
#                 break
#         else:
#             idx_now += 1
# lst = [-88, 41, -6, -96, 42, 96, 38, -38, 28, 72]
# arr_copy = lst.copy()
# arr2 = [6,12,4,3,8]





#сортировка пузырьком через while
arr = [-95, 16, 15, 88, 1, -93, -20, 5, -10, -49, 4, -43, 2, 29, -96, 33, -55, 73, 52, -1]
def bubble_while(lst):
    n = len(lst) - 1
    idx = 0
    while idx < n:
        while lst[idx] > lst[idx + 1]:
            print(lst)
            print(idx)
            lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
            idx = 0 if lst[idx] < lst[idx + 1] else idx + 1
        idx += 1
    return lst
print(bubble_while(arr))
# #Сортировка пузырьком через for
#
# def bubble_for(lst):
#     for i in range(10):
#         for j in range(10):
#             if j < 9 and lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
# print(bubble_for(arr_copy))

#Сортировка пузырьком комбинированная
# arr_copy_2 = arr_copy.copy()
# def bubble_combo(lst):
#     for i in range(len(lst)):
#         n = 0
#         while n < len(lst):
#             if n < 9 and lst[n] > lst[n + 1]:
#                 lst[n], lst[n + 1] = lst[n + 1], lst[n]
#             n += 1
#     return lst
# print(bubble_combo(arr_copy_2))



# lst = [-88, 41, -6, -96, 42, 96, 38, -38, 28, 72]
# arr_copy = lst.copy()
# arr2 = [6,12,4,3,8]
#сортировка шейкером

# def shaker_sort(lst):
#     for i in range(len(lst)):
#         n = i
#         while n < len(lst) - i - 1:
#             if lst[n] > lst[n + 1]:
#                 lst[n], lst[n + 1] = lst[n + 1], lst[n]
#             n += 1
#         n = -i - 1
#         while n > -len(lst) + i:
#             if lst[n - 1] > lst[n]:
#                 lst[n - 1], lst[n] = lst[n], lst[n - 1]
#             n -= 1
#     return lst
# print(shaker_sort(lst))

#рекурсивная сортировка
# lst = [-88, 41, -6, -96, 42, 96, 38, -38, 28, 72]
# arr_copy = lst.copy()
# arr2 = [6,12,4,3,8]
# l = []
# def test(*args):
#     print(args)
#     if len(args[0]) <= 1:
#         return args
#
#     if len(args) == 1:
#         middle = len(args[0]) // 2
#         left = args[:middle]
#         right = args[middle:]
#     else:
#         mid_left, mid_right = len(args[0]) // 2, len(args[1]) // 2
#         left_left, right_left = args[0][:mid_left], args[0][mid_left:]
#         right_right, left_right = args[1][:mid_right], args[1][mid_right:]

    # return test(left, right)



#     l.append([left, right])
#     return test(left, right)
# print(test(lst))
# print(l)




# def double(lst):
#     if len(lst) == 1:
#         if not sort_lst:
#             sort_lst.append(lst[0])
#
#         else:
#             if lst[0] < sort_lst[0]
#         return lst
#     middle = len(lst) // 2
#     left = lst[:middle]
#     right = lst[middle:]
#     return double(left), double(right)
# print(double(at))
# print(sort_lst)
# def foo(left,right):
#     print(f'в функции слияния {left}, {right}')
#     sorted_lst = []
#     left_idx = right_idx = 0
#     for i in range(len(left) + len(right)):
#         if left_idx < len(left) and right_idx < len(right):
#             if left[left_idx] <= right[right_idx]:
#                 sorted_lst.append(left[left_idx])
#                 left_idx += 1
#             else:
#                 sorted_lst.append(right[right_idx])
#                 right_idx += 1
#         elif left_idx == len(left):
#             sorted_lst.append(right[right_idx])
#             right_idx += 1
#         else:
#             sorted_lst.append(left[left_idx])
#             left_idx += 1
#     print(sorted_lst)
#     return sorted_lst


# print(at)
# def double(lst):
#     if len(lst) <= 1:
#         print(f'flag')
#         return lst
#     middle = len(lst) // 2
#
#     left = double(lst[:middle])
#
#     right = double(lst[middle:])
#
#     return foo(left, right)
# print(double(at))


#сортировка Хоара
# at = [39, 32, 44, 63, -21, -76, -56, -70, -36, -57, -46, -83, -31, 35, -91, 100, 99, -56, 69, 93]
#
# def quick_sort(lst):
#     print(lst)
#
#     if len(lst) <= 1:
#
#         return lst
#
#
#
#     element = random.choice(lst)
#     L, M, R = [], [], []
#     for step in lst:
#         if step < element:
#             L.append(step)
#         elif step > element:
#             R.append(step)
#         else:
#             M.append(step)
#     # print(f'{L}    {M}     {R}')
#     if len(L) == 0:
#         print(True)
#     return quick_sort(L) + M + quick_sort(R)
# print(quick_sort(at))
# at[0] = str(at[0])
# print(at)
#
# def foo(lst, idx):
#     if idx == len(lst):
#         return lst
#     lst[idx] = str(lst[idx])
#     idx += 1
#     return foo(lst, idx)
#
# print(foo(at, 0))
#стандартная сортировка питон
at = [39, 32, 44, 63, -21, -76, -56, -70, -36, -57, -46, -83, -31, 35, -91, 100, 99, -56, 69, 93]
def standart(lst):
    lst.sort()
    return lst
print(standart(at))