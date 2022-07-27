#Вычислить число π c заданной точностью d

acc = list(input("Задайте точность для вычисления pi: "))

n = len(acc)-2

pi = round(sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n)), n)

print(pi)