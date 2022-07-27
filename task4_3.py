# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
min = 1
max = 10
size = 20

my_list = [randint(min,max) for i in range(size)]

uniq_list =[]
for i in range(len(my_list)):
    count = 0
    for j in my_list:
        if my_list[i] == j: count +=1
    if count == 1:
        uniq_list.append(my_list[i])

print(f'Случайный ряд:            {my_list}')
print(f'Ряд без повторений:       {set(my_list)}')
print(f'Неповторяющиеся элементы: {uniq_list}')