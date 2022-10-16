import random
# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
print('\nЗадание 4')
listA = []
number = int(input('Введите число: '))
for i in range(0, number):
    new_element = random.randrange(-number, number)
    listA.append(new_element)
print(
    '\nCписок из N элементов, заполненных числами от -N до N:\n',
    f'{listA}\n')
b = []
path = 'file.txt'
data = open(path, 'r')
for line in data:
    b.append(int(line))
data.close()
print('Cписок индексов из file.txt:\n', f'{b}\n')
multiplication = 1
for i in b:
    if number < i:
        i = i + 1
    else:
        multiplication *= listA[i]
print('Произведение элементов на указанных позициях: ', f'{multiplication}\n')
