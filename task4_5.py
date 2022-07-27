#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


from random import randint
import itertools
import re

Poly1File = 'Polynomial34_1.txt'
Poly2File = 'Polynomial34_2.txt'
PolySumFile = 'Polynomials34_Sum.txt'

k = int(input("Введите натуральную степень для многочленов: "))

def form_ratio_list(ratio):
    ratios_list = list([randint(0, 101) for i in range(ratio+1)])
    if ratios_list[0] == 0:
        ratios_list[0] = randint(1, 101)
    return ratios_list

#Формирование многочлена 
def get_polynomial(k, ratio_list):
    var = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio_list, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x',' x')

#Получение кортежей коэф и степень
def cort_kef_rait(poly):
    poly = poly.replace('= 0', '')
    poly = re.sub("[*|^| ]", " ", poly).split('+')
    poly = [char.split(' ') for char in poly]
    poly = [[x for x in list if x] for list in poly]
    for i in poly:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    poly = [tuple(int(x) for x in j if x != 'x') for j in poly]
    return poly

#Получение кортежей суммы - коэф1+коэф, степень
def sumkefrait(poly1, poly2):   
    x = [0] * (max(poly1[0][1], poly2[0][1] + 1))
    for i in poly1 + poly2:        
        x[i[1]] += i[0]
    result = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    result.sort(key = lambda r: r[1], reverse = True)
    return result

#Суммирование многочленов
def SumPoly(poly):
    var = ['*x^'] * len(poly)
    coefs = [x[0] for x in poly]
    degrees = [x[1] for x in poly]
    sumpoly = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in sumpoly:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    sumpoly = list(itertools.chain(*sumpoly))
    sumpoly[-1] = ' = 0'
    return "".join(map(str, sumpoly))

#Создание файлов с многочленами
with open(str(Poly1File), 'w') as data:
    data.write(get_polynomial(k, form_ratio_list(k)))
with open(str(Poly2File), 'w') as data:
    data.write(get_polynomial(k, form_ratio_list(k)))

#Чтение многочленов из файлов
with open(str(Poly1File), 'r') as data:
        poly1 = data.read()
with open(str(Poly2File), 'r') as data:
        poly2 = data.read()

polysum = SumPoly(sumkefrait(cort_kef_rait(poly1),cort_kef_rait(poly2)))

with open(str(PolySumFile), 'w') as data:
    data.write(polysum)

print(poly1)
print(poly2)
print(polysum)
