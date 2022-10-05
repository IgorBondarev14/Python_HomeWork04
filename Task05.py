# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

k1 = int(input("задайте степень многочлена: "))
m1 = 0
from sympy import *
x = Symbol('x')
import random
for i in range(0, k1 + 1):
    m1 = m1 + random.randint(-10, 11) * x ** i
print("y = ", str(m1))

k2 = int(input("задайте степень многочлена: "))
m2 = 0
from sympy import *
x = Symbol('x')
import random
for i in range(0, k2 + 1):
    m2 = m2 + random.randint(-10, 11) * x ** i
print("y = ", str(m2))

data1 = open('m1.txt', 'w')
data1.write(str(m1))
data1.write("\n")  
data1.close()
data2 = open('m2.txt', 'w')
data2.write(str(m2))
data2.write("\n")  
data2.close()



# result = open('sum.txt', 'w')
# result.write(str(data1) + (strdata2))
# result.close()
exit()