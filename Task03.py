# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

#sequence = input("Введите последовательность чисел: ").split()


from random import randint
n = int(input("Введите размер последовательности: "))
sequence = []
for i in range(n):
    sequence.append(randint(1, 20))
print(sequence)

unique_sequence = []
for i in range(n):
    if sequence.count(sequence[i]) == 1:
        unique_sequence.append(sequence[i])
print(unique_sequence)

