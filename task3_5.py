#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. 

num = int(input('Введите число: '))

neg_num = - num

listFib = []

def FibMinus(n):
    if n == -1: return 1
    elif n == -2: return -1
    return FibMinus (n + 2) - FibMinus (n + 1) 

def FibPlus(n):
    if n in [1,2]:
        return 1
    elif n == 0:
        return 0
    else:
        return FibPlus(n-1) + FibPlus(n-2)

for i in range(neg_num, num + 1):
    if i < 0:
        listFib.append(FibMinus(i))
    else:
        listFib.append(FibPlus(i))    

print (listFib)