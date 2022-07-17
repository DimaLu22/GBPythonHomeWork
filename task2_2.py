# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число N:' ))
i = 1

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

while i <= n:
    print(f'{i} -> {factorial(i)}')
    i += 1