import random
#бинарное дерево которое сортирует список
arr = [8, 6, 14, 1, 10, 2, 7, 3, 11, 5, 13, 15, 12, 0, 9, 4]
# test_arr = [random.randint(-100, 100) for _ in range(100)]
arr_new = []

branch = -1

#нужно из отсортированного списка сделать дерево
class BinTree:
    def __init__(self, core, *el):
        #узел, левая ветвь, правая ветвь
        self.core, self.left, self.right = core, None, None
        #более лакончиное решение. Сделано, чтобы уйти от elif

        #Это распределение приходящих элементов в новом списке, который в конце будет отсортированным.
        movement_along_branches = {
            'root': lambda : arr_new.insert(0, self.core),
            'L': lambda : arr_new.insert(el[1], self.core),
            'R': lambda : arr_new.insert(el[1] + 1, self.core)
        }
        movement_along_branches.get(el[0])()
        #классическое решение (некрасивое)
        # if el[0] == 'root':
        #     arr_new.insert(0, self.core)
        #
        # elif el[0] == 'L':
        #     arr_new.insert(el[1], self.core)
        #
        # elif el[0] == 'R':
        #     arr_new.insert(el[1] + 1, self.core)
    #метод для создания нового узла
    def make_branch(self, new_core):
        #если праваметр меньшем ядра на текущем ходе рекурсии, то проваливаемся в условие:
        if new_core < self.core:
            #если левого узла не существует, то сохраняем индекс текущего узла в списке в переменную idx.А потом создаем
            #новый экземпляр класса self.left с параметрами:
            # текущий параметр метода(цифра из списка)
            # буква, показывающая направление (влево т.е внизу по дереву)
            # idx - индекс для последующей работы с ним в словаре movement_along_branches
            if self.left is None:
                idx = arr_new.index(self.core)
                self.left = BinTree(new_core, 'L', idx)
            # Если левый узел есть - переходим на него(на уровень ниже) и кидаем скрипт создания
            # нового узла опираясь уже на него. Рекурсивно повторяем эти действия, пока не упремся в условие с None (выше)
            else:
                self.left.make_branch(new_core)
        else:
            #Тут практически все то же самое, что и выше с той лишь разницей, что idx мы создаем по другому. Мы находим
            #индекс последнего вхождения self.core в списке, который мы строим в том случае, когда этих ядер (цифр) в списке
            # у нас больше одного. Иначе берем первое и единственное вхождение (через index)
            if self.right is None:
                if arr_new.count(self.core) > 1:
                    idx = arr_new.index(self.core) + arr_new.count(self.core) - 1
                #если количество чисел в списке больше одного, то мы находим индекс последнего вхождения этого
                #числа в список(self.core). Этот индекс мы кидаем в создание нового узла (el[1]) в __init__. Прибавляем единицу
                # и ставим узел(новый self.core) справа от self.core, индекс которого мы нашли в списке.
                else:
                    idx = arr_new.index(self.core)
                self.right = BinTree(new_core, 'R', idx)
            else:
                self.right.make_branch(new_core)
arr_sorted = list(sorted(arr))
tree = BinTree(min(test_arr), 'root', 0)

for item in test_arr[1:]:
    tree.make_branch(item)


if arr_new == list(sorted(test_arr)):
    print(f'список правильно отсортирован!')
print(list(sorted(test_arr)))
print(f'новый список {arr_new}')








# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15


#                           8
#                       4       12
#                     2   6   10  14
#                    1 3 5 7 9 11 13 15


# class BinaryTree:
#     def __init__(self, root_obj):
#         # корень
#         self.root = root_obj
#         # левый потомок
#         self.left_child = None
#         # правый потомок
#         self.right_child = None
#
#     # добавить левого потомка
#     def insert_left(self, new_node):
#         # если у узла нет левого потомка
#         if self.left_child is None:
#             # тогда узел просто вставляется в дерево
#             # формируется новое поддерево
#             self.left_child = BinaryTree(new_node)
#         # если у узла есть левый потомок
#         else:
#             # тогда вставляем новый узел
#             tree_obj = BinaryTree(new_node)
#             # и спускаем имеющегося потомка на один уровень ниже
#             tree_obj.left_child = self.left_child
#             self.left_child = tree_obj
#
#     # добавить правого потомка
#     def insert_right(self, new_node):
#         # если у узла нет правого потомка
#         if self.right_child is None:
#             # тогда узел просто вставляется в дерево
#             # формируется новое поддерево
#             self.right_child = BinaryTree(new_node)
#         # если у узла есть правый потомок
#         else:
#             # тогда вставляем новый узел
#             tree_obj = BinaryTree(new_node)
#             # и спускаем имеющегося потомка на один уровень ниже
#             tree_obj.right_child = self.right_child
#             self.right_child = tree_obj
#
#     # метод доступа к правому потомку
#     def get_right_child(self):
#         return self.right_child
#
#     # метод доступа к левому потомку
#     def get_left_child(self):
#         return self.left_child
#
#     # метод доступа к корню
#     def get_root_val(self):
#         return self.root
#
#
# r = BinaryTree(8)
# print(r.get_root_val())
# print(r.get_left_child())
# r.insert_left(25)
# print(r.get_left_child())
# print(r.get_left_child().get_root_val())
# r.insert_right(6)
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# print(r.get_right_child().get_root_val())
