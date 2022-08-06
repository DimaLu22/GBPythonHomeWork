# Создайте программу для игры с конфетами человек против умного бота. Условие задачи: На столе лежит 2021 конфета. 
# Играет человек против бота ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

from random import randint

player1 = input('Введите Ваше имя: ')
player2 = 'Умнейший БОТ'
quant_cand = 140
max_take_cand = 28

def takes_candys(name):
    x = int(input(f"{name}, введите количество конфет 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, количество должно быть от 1 до 28: "))
    return x

def calc_for_bot(quant):
    q = randint(1, 29)
    if quant > 56:
        while (quant - q)%28 != 0:
            q = randint(1, 28)
    else:
            q = quant - 29
    if q == 0:
        q = 1
    return q

priority = randint(0,1)

if priority:
    print(f'Первым ходит: {player1}')
else:
    print(f'Первым ходит: {player2}')

while quant_cand > max_take_cand:
    if priority:
        num_cand = takes_candys(player1)
        quant_cand -= num_cand
        priority = False
        print(f'{player1} взял(а) {num_cand}, на столе осталось {quant_cand} шт')
    else:
        num_cand = calc_for_bot(quant_cand)
        quant_cand -= num_cand
        priority = True
        print(f'{player2} взял(а) {num_cand}, на столе осталось {quant_cand} шт')

if priority:
    print(f'Победа за {player1}')
else:
    print(f'Победа за {player2}')