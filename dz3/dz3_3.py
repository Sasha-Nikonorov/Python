# 3.Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] = > 0.20

lst = [1.1, 1.2, 3.1, 5, 10.01]

temp = lst[0] % 1

minEl = temp
maxEl = temp

for i in lst:
    temp = i % 1
    if temp < minEl:
        minEl = temp
    if temp > maxEl:
        maxEl = temp

result = maxEl - minEl
print('%.2f' % result)
