# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num_quard = int(input('Введите номер четверти: ' ))
while num_quard < 1 or num_quard > 4:
    print('Please, enter integer number beetwen 1 and 4: ')
    num_quard = int(input())

diapasones = ['(x > 0, y > 0)', '(x < 0, y > 0)', '(x < 0, y < 0)', '(x > 0, y < 0)']
print(f'{num_quard}: {diapasones[num_quard-1]}')