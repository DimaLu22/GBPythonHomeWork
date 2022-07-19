# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

my_list = list(map(int, input("Введите числа через пробел:\n").split()))

def sum_odd_ind(lst):
    sum = 0
    for i in range(len(lst)):
        if i%2 != 0:
            sum += lst[i]
    return sum

print(f'Сумма элементов на нечетных позициях равна: {sum_odd_ind(my_list)}')
