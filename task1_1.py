# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input('Введите день недели:'))
while number < 1 or number > 7:
    print('Please, enter integer number beetwen 1 and 7: ')
    number = int(input())
if number == 6 or number == 7:
    print('Да')
else:
    print('Нет')