# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

bin_num = ""

dec_num = int(input("Введите десятичное число:\n"))

while dec_num != 0:
    bin_num = str(dec_num%2) + bin_num
    dec_num //=2

print(f'Двоичное число: {bin_num}')