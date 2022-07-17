# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input('Введите число N:' ))
i = 1
sum = 0
listN = []

def func(number: int):
    res = round((1+1/number)**number, 3)
    return res

while i <= n:
    listN.append(func(i))
    sum += func(i)
    i += 1

print(f'Ряд: {listN}')
print(f'Сумма чисел ряда: {sum}')