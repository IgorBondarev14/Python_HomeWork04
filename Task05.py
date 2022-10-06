# # Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# k1 = int(input("задайте степень многочлена: "))
# m1 = 0
# from sympy import *
# x = Symbol('x')
# import random
# for i in range(0, k1 + 1):
#     m1 = m1 + random.randint(-10, 11) * x ** i
# print("y = ", str(m1))

# k2 = int(input("задайте степень многочлена: "))
# m2 = 0
# from sympy import *
# x = Symbol('x')
# import random
# for i in range(0, k2 + 1):
#     m2 = m2 + random.randint(-10, 11) * x ** i
# print("y = ", str(m2))

# data1 = open('m1.txt', 'w')
# data1.write(str(m1))
# data1.close()
# data2 = open('m2.txt', 'w')
# data2.write(str(m2))
# data2.close()

data1 = open('m1.txt', 'r')
mnogochlen1 = str(*data1)
print(mnogochlen1)
data1.close()
data2 = open('m2.txt', 'r')
mnogochlen2 = str(*data2)
print(mnogochlen2)
data2.close()

if mnogochlen2[0] != '-':
    sum_mnogochlen = mnogochlen1 + ' + ' + mnogochlen2
else:
    sum_mnogochlen = mnogochlen1 + ' ' + mnogochlen2
summa = sum_mnogochlen.split()
print(summa)

index_pl = []
for i in range(0, len(summa)):
    if summa[i] == '+':
        index_pl.append(i)
for i in range(len(index_pl)):
    del summa[int(index_pl[i])]
print(summa)

for i in range(len(summa)):
    if summa[i] == '-':
        summa[i + 1] = '-' + summa[i + 1]
index_min = []
for i in range(len(summa)):
    if summa[i] == '-':
        index_min.append(i)

for i in range(len(index_min)):
    del summa[int(index_min[i])]
print(index_min)
