# 2. Напишите программу для. проверки истинности утверждения not (X or Y
# or Z) = not X and not Y and not Z для всех значений предикат.

print('Задание 2')

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'X = {x}, Y = {y}, Z = {z}',
                  not (x or y or z) == (not x and not y and not z))
