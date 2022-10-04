# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число '))
konvert = ''
while number > 0:
    konvert = str(number % 2) + konvert
    number //= 2
print(konvert)
