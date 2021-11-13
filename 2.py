#3 задача 31 вар
K = int(input('Введите K = '))
F1 = 1
F2 = 1
F = 0
while F < K:
    F = F1 + F2
    F2 = F1
    F1 = F
print (F2,F1 + F2)  
