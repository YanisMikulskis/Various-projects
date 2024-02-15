# n = 11
# var = 0
# var_2 = 0
# a_dict = {
#     '1': 'пн',
#     '2': 'вт',
#     '3': 'ср',
#     '4': 'чт',
#     '5': 'пт',
#     '6': 'cб',
#     '7': 'вс'
# }
# def Foo():
#     global var, var_2
#     var_2 += 1
#     for k, v in a_dict.items():
#         print(var_2)
#         # if var_2 == n:
#         #     print(v)
#     return var_2
# for i in range(1, len(a_dict) + 1):
#     Foo()
#     print(Foo())
#     if i == len(a_dict):
#         for j in range(0, n - len(a_dict)):
#             print(Foo() + j)



#пт
n = 27 #вводим любое число
#Брусничка, дерзай))
arr = [1, 77, 3, 4, 9]

if type(n) == int:


    if 0 < n <= len(arr) - 1:
        print(arr[n])
    else:
        for i in range(1, n//len(arr) + 1):


            for j in arr:
                ...
            if i == n//len(arr):
                remainder = n - (i*len(arr)-1)
                print(arr[:remainder][-1])


else:print(f'Число должно быть целым')
# если 27 то должно выводить 3
#если 28 то выводит 4