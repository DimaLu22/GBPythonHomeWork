# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = list(map(int, input("Введите числа через пробел:\n").split()))

def mult_lst(lst):
    new_lst = []
    if len(lst) % 2 != 0:
        num_par = len(lst)//2 + 1 
    else: 
        num_par = len(lst)//2
    
    for i in range(num_par):
        new_lst.append(lst[i]*lst[len(lst)-i-1])
    return new_lst

print(f'Произведения пар чисел списка: {mult_lst(my_list)}')