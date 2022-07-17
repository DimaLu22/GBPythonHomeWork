#Реализуйте алгоритм перемешивания списка.

from random import randint


list = ['1', 'Привет', '2', 'До свидания', '3', 'И снова здравствуйте', '4', 'Финита']
def shuflist(listA: list):
    listB = listA[:]
    for i in range(len(listA)):
        j = randint(0, len(listA)-1)
        listB[i] = listA[j]
        del listA[j]
    return listB

print(list) 
print(shuflist(list))
