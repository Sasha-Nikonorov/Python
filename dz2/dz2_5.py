import random
# 5. Реализуйте алгоритм перемешивания списка
print('Задание 5')
listA = []
number = int(input('Введите число: '))
for i in range(1, number + 1):
    new_element = random.randrange(-number, number)
    listA.append(new_element)
print(
    '\nCписок из N элементов, заполненных числами от -N до N:\n',
    f'{listA}\n')
random.shuffle(listA)
print('Перемешанный список:\n', listA)
