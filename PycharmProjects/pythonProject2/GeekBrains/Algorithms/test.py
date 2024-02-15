import datetime
import re
from datetime import timedelta

from pyheat import PyHeat
def foo(*args):
    d_word, h_word, m_word = ('дня', 'дней'), ('часа', 'часов'), ('минуты', 'минут')

    lam = lambda start, end, step: list(range(start, end, step))
    end_1 = lam(1, 52, 10)
    end_2_4 = [*lam(22, 53, 10), *lam(23, 54, 10), *lam(24, 55, 10)]

    other_d = lambda d: d_word[0] if d in end_2_4 else d_word[1]
    other_h = lambda h: h_word[0] if h in end_2_4 else h_word[1]
    other_m = lambda m: m_word[0] if m in end_2_4 else m_word[1]

    if len(args) == 3:
        d = 'день' if args[0] in end_1 else other_d(args[0])
        if not args[1]:
            return f'{args[0]} {d}'
        else:
            h = 'час' if args[1] in end_1 else other_h(args[1])
            return f'{args[0]} {d} {args[1]} {h}'

    elif len(args) == 2:
        h = 'час' if args[0] in end_1 else other_h(args[0])
        m = 'минута' if args[1] in end_1 and args[1] != 11 else other_m(args[1])
        return f'{args[0]} {h} {args[1]} {m}'

    else:
        m = 'минута' if args[0] in end_1 else other_m(args[0])
        return f'{args[0]} {m}'


# 01.10.2023 19:47
# 30.09.2023 20:47
# 15.10.2023 19:47
# текущее время + 1 день
while 1:
    date_test = input(f'введите дату: ')
    req = re.findall(r'^\d{2}[.]\d{2}[.]\d{4}\s\d{2}[:]\d{2}$', date_test)

    if req:
        date_test_time = datetime.datetime.strptime(date_test, "%d.%m.%Y %H:%M")
        data_now = datetime.datetime.now()
        if date_test_time < data_now:
            print(f'Ошибка! Дата меньше минимальной (текущей)')
            continue

        result = date_test_time - data_now
        day, hour, minute = result.days, result.seconds // 3600, result.seconds % 3600 // 60

        if day:
            print(f'До часа X1 {foo(day, hour, minute)}')
            break

        else:
            if hour:
                if data_now + timedelta(days=1) - date_test_time < timedelta(minutes=1):  # ключевое выражение
                    print(f'До часа XXX 1 день')
                    break
                print(f'До часа х {foo(hour, minute)}')
                break
            else:
                if minute:
                    print(f'До часа X {foo(minute)}')
                    break

    else:
        print(f'Ошибка типа')
# ph = PyHeat('test.py')
# ph.create_heatmap()
# ph.show_heatmap()