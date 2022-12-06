# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#     *Пример:*

#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

import random

lst = random.sample(range(10), 5)
print(lst)

# lst = [2, 3, 4, 5, 6]
# print(lst)

new_len = 0
if len(lst)%2 == 0:
    new_len = len(lst)//2
else:
    new_len = len(lst)//2+1

for i in range(new_len):
    new_lst = lst[i] * lst[len(lst) - i - 1]
    print(new_lst)