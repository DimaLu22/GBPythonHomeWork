# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def encod(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

def decod(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

with open('decoded_RLE.txt', 'r') as data:
    text_deco = data.read()

with open('encoded_RLE.txt', 'r') as data:
    text_code = data.read()

str_code = encod(text_code)
print(str_code)

str_decode = decod(text_deco)
print(str_decode)