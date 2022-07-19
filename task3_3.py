# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

my_list = list(map(float, input("Введите вещественные числа через пробел:\n").split()))

frac_part = []

for i in my_list:
    if i%1 != 0:
        frac_part.append(round(i%1,2))

print(max(frac_part)-min(frac_part))