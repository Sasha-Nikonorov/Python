# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

candy = 221

print(f'На столе лежит {candy} конфета.\n'
      f'Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\n'
      f'За один ход можно забрать не более чем 28 конфет.\n'
      f'Все конфеты оппонента достаются сделавшему последний ход.\n')

player1 = input("Введите имя первого игрока: ")
all_player1candy = 0
player2 = input("Введите имя второго игрока: ")
all_player2candy = 0

draw = random.randint(1, 2)
first = draw

print(f'Начинает игрок под номером: {draw}')

if first == 1:
    print(f'{draw} игрок берет конфеты')

else:
    print(f'{draw} игрок берет конфеты')

while candy > 0:
    print(f'Конфет осталось {candy}\n')
    player1candy = int(input(f'Игрок {player1} берет:'))
    if 0 < player1candy > 28:
        player1candy = int(input("Не верное количество конфет"))
    all_player1candy += player1candy
    print(f'Количество конфет игрока {player1} = {all_player1candy}\n')
    candy += -player1candy

    print(f'Конфет осталось {candy}\n')
    player2candy = int(input(f'Игрок {player2} берет:'))
    if 0 < player2candy > 28:
        player1candy = int(input("Не верное количество конфет"))
    all_player2candy += player1candy
    print(f'Количество конфет игрока {player2} = {all_player2candy}\n')
    candy += -player2candy

# if candy == 0:
