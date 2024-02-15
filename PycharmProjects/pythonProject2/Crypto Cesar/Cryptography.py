# Шифр Цезаря. Каждый буква в сообзении двигается влево или в право на определнное количество символов
import re

letters = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

mess = 'Привет, World!'


def encrypt(arg_mes, k):
    arg_mes = ''.join(map(lambda x: x.upper() if x.upper() in letters else x, arg_mes))
    new_mes = ''
    for let in arg_mes:
        if let in letters:
            if letters.index(let) + k not in [i for i in range(len(letters))]:
                new_mes += letters[(letters.index(let) + k) % len(letters)]
            else:
                new_mes += letters[letters.index(let) + k]
        else:
            new_mes += let
    return new_mes


print(encrypt(mess, 5))

# letters2 = ''.join(map(lambda x:x.upper() if x in re.findall(r'[а-яА-ЯёЁ]', mess) else x.lower(), mess))
