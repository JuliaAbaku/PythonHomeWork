# Задайте последовательность чисел. 
# Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

import random
 
list1 = []

for i in range(7):
    a = random.randint(0,5)
    list1.append(a)
print(list1)

list2 = []

for i in range(len(list1)):
    if list1.count(list1[i]) == 1:
        list2.append(list1[i])
print(list2)

