# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input('Введите число N:' ))
i = 1
sum = 0
listN = []

# def func(number: int):
#     res = round((1+1/number)**number, 3)
#     return res

#listN = [func(i) for i in range(1, n+1)]

# while i <= n:
#     listN.append(func(i))
#     sum += func(i)
#     i += 1

#Оптимизированный код
print(f'Ряд: {[round((1+1/i)**i, 3) for i in range(1, n+1)]}')
while i <= n:
    sum += round((1+1/i)**i, 3)
    i += 1
print(f'Сумма чисел ряда: {sum}')