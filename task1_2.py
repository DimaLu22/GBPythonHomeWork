# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#Решение задачи через if
# def logic(x, y, z):
#     print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}')
#     return (not (x or y or z)) == (not x and not y and not z)
# if (logic(0, 0, 0) and logic(0, 0, 1) and logic(0, 1, 0) and 
#     logic(0, 1, 1) and logic(1, 0, 0) and logic(1, 0, 1) and
#     logic(1, 1, 0) and logic(1, 1, 1)):
#     print('TRUE')
# else:
#     print('FALSE')

#Решение через for
for x in range(2):
    for y in range(2):
     for z in range(2):
        print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} -> {(not (x or y or z)) == (not x and not y and not z)}')