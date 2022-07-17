# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции задаются с клавиатуры через пробел.

from random import randint

mult = 1
n = int(input('Введите число N: '))
listN = [0]*n

for i in range(n):
    listN[i] = randint(-n, n)
print(f'Список из {n} элементов: {listN}')

poss = input('Введите позиции через пробел: ') #Позиция от 1 до N
for j in range(len(poss)):
    if poss[j] != ' ':
        mult *= listN[int(poss[j])-1]

print(f'Произведение элементов на выбраных позициях: {mult}')