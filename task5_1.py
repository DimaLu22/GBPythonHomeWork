# Напишите программу, удаляющую из текста все слова, содержащие ""абв"". Задача была решена на семинаре.
#Два варианта решения задачи!

word = 'абв Ура, питон круто, очень интересные семинарыабв ! абв'
find = 'абв'

#По старинке:)
def del_words(my_word, del_text):
    my_word = list(filter(lambda x: del_text not in x, my_word.split()))
    return " ".join(my_word)
print(del_words(word, find))

#По взрослому!
word = word.split()
f = lambda x: not x.count(find) > 0
print(' '.join(list(filter(f, word))))