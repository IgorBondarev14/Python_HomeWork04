# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input("задайте степень многочлена: "))
mnogochlen = 0
from sympy import *
x = Symbol('x')
import random
for i in range(0, k + 1):
    mnogochlen = mnogochlen + random.randint(-10, 11) * x ** i
print("y = ", str(mnogochlen))

data = open('file.txt', 'w')
data.write("y = ")
data.write(str(mnogochlen))
data.write("\n")  
data.close()
exit()
