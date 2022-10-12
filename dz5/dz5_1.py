# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# data = input('Введите текст: ')

data = 'Напишите программу, удаляющую ""абв"" . ' \
       'стул, стол, ананас, батут, обнова, швабра, автобус, забвение, зимбабве, вомбат, нос'
temp = data.lower().split(' ')

# не понял задание. нужно было убрать слово в котором есть все эти 3 буквы
# или она из букв. сделал и так и так

a, b, v = 'а', 'б', 'в'
lst = []

# for i in temp:
#     if a not in i:
#         if b not in i:
#             if v not in i:
#                 lst.append(i)

for i in temp:
    if a and b and v not in i:
        lst.append(i)
lst[0] = lst[0].capitalize()
result = ' '.join(lst)

print(result)
