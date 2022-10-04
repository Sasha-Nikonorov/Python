# 4. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

print('Задание 4')

numberquarter = int(input('Введите номер четверти: '))
match numberquarter:
    # case 0:
    # return 'центр координат'
    case 1:
        print('x > 0, y > 0')
    case 2:
        print('x < 0, y > 0')
    case 3:
        print('x < 0, y < 0')
    case 4:
        print('x > 0, y < 0')
    case _:
        print('такой четверти нет')
