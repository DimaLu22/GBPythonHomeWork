# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k.
from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))

ratios_list = list([randint(0, 101) for i in range(k+1)])
if ratios_list[0] == 0:
    ratios_list[0] = randint(1, 101)


def get_polynomial(k, ratio_list):
    var = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio_list, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x',' x')


polynomial = get_polynomial(k, ratios_list)
print(polynomial)

with open('Polynomial.txt', 'w') as data:
    data.write(polynomial)