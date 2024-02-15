import copy
import random
from collections import Counter, deque
import numpy as np

# -------------------------------------КОДИРОВКА ПО ХОФФМАНУ------------------------------------------
# бинарное дерево которое сортирует список

# -----------
text = 'beep boop beer!'


# общие функции для вывода
def foo(el, table, code):
    if not isinstance(el, dict):
        table.setdefault(el, code)
        return
    foo(el.get(0), table, code=code + '0')
    foo(el.get(1), table, code=code + '1')


def select_code(string_arg, step=0):
    for i in range(4, len(string_arg) + 4, 4):
        string_arg.insert(i + step, ' ')
        step += 1


# Алгоритм Хаффмана через цикл while
# ------------------------------------------------
def Haffman_cyclo(arg_text=text):
    text_counter = Counter(arg_text).items()
    symbol_freq = deque(list(sorted(text_counter, key=lambda item: item[1])))

    def BinTree(arg_arr):
        while len(arg_arr) > 1:
            core = arg_arr[0][1] + arg_arr[1][1]
            left_sheet, right_sheet = arg_arr.popleft()[0], arg_arr.popleft()[0]
            sheets = {
                0: left_sheet,
                1: right_sheet
            }
            core_sheets = (sheets, core)
            for idx, count in enumerate(symbol_freq):
                if core > count[1]:
                    continue
                else:
                    symbol_freq.insert(idx, core_sheets)
                    break
            else:
                symbol_freq.append(core_sheets)
        return symbol_freq

    BinTree(symbol_freq)
    return symbol_freq.popleft()[0]


code_table = {
}

foo(Haffman_cyclo(), code_table, '')
code_string = list(''.join([code_table.get(i) for i in text]))
select_code(code_string)
final_code = ''.join(code_string)
print(final_code)
print()

# алгоритм Хаффмана через ООП
# ------------------------------------------------
text_2 = copy.copy(text)


def OOP(arg_text=text_2):
    counter_text = Counter(arg_text).items()
    symbol_freq, global_message = deque(list(sorted(counter_text, key=lambda item: item[1]))), []

    class BinTree:
        def __init__(self, *letters):
            if letters:
                self.left, self.core, self.right = letters[0], letters[1], letters[2]
                self.sheets = {
                    0: self.left,
                    1: self.right
                }

        @staticmethod
        def make_tree(message):
            if len(message) <= 1:
                global_message.append(message[0][0])
                return global_message
            core = message[0][1] + message[1][1]
            sheet = BinTree(message.popleft()[0], core, message.popleft()[0])
            result = (sheet.sheets, core)
            for idx, count in enumerate(symbol_freq):
                if core > count[1]:
                    continue
                else:
                    message.insert(idx, result)
                    break
            else:
                message.append(result)
            BinTree.make_tree(message)

    bin = BinTree()
    bin.make_tree(symbol_freq)
    return global_message[0]


code_table_2 = {
}
foo(OOP(), code_table_2, '')
code_string_2 = list(''.join([code_table_2.get(i) for i in text_2]))

select_code(code_string_2)
final_code_2 = ''.join(code_string_2)
print(final_code_2)
