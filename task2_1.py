# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input('Введите вещественное число: ')
# sum = 0
# for i in range(len(number)):
#     if number[i] != ',':
#         sum += int(number[i])
# print(f'{number} -> {sum}')

n = sum(map(int, list(str(number).replace(',',''))))
print(f'{number} -> {n}')
