# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

player1 = input('Имя первого игрока: ')
player2 = input('Имя второго игрока: ')
quant_cand = 2021
max_take_cand = 28



def takes_candys(name):
    x = int(input(f"{name}, введите количество конфет 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, количество должно быть от 1 до 28: "))
    return x

priority = randint(0,1)

if priority:
    print(f'Первым ходит: {player1}')
else:
    print(f'Вторым ходит: {player2}')

while quant_cand > max_take_cand:
    if priority:
        num_cand = takes_candys(player1)
        quant_cand -= num_cand
        priority = False
        print(f'{player1} взял(а) {num_cand}, на столе осталось {quant_cand} шт')
    else:
        num_cand = takes_candys(player2)
        quant_cand -= num_cand
        priority = True
        print(f'{player2} взял(а) {num_cand}, на столе осталось {quant_cand} шт')

if priority:
    print(f'Победа за {player1}')
else:
    print(f'Победа за {player2}')