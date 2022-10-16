# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
import random

lst1 = []
number = int(input('Введите число: '))
for i in range(number):
    new_element = random.randrange(1, number)
    lst1.append(new_element)
print(lst1)
lst2 = []
for i in lst1:
    if lst1.count(i) < 2:
        lst2.append(i)
print(lst2)
