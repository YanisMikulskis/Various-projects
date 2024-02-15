from collections import Counter, deque

text = 'beep boop beer!'


# алгоритм Хаффмана через ООП
def OOP(arg_text=text):
    counter_text = Counter(arg_text).items()
    symbol_freq = deque(list(sorted(counter_text, key=lambda item: item[1])))

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
                print(f'дерево {message[0][0]}')
                return
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
OOP()
