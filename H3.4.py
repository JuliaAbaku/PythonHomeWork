# Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#     *Пример:*

#     - для k = 8 список будет выглядеть так: 
#     [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число '))

pos_fib = []
neg_fib = []

a, b = 0, 1
c, d = 0, 1


for i in range(k):
    a, b = b, a+b
    pos_fib.append(a)
    c, d = d, c - d
    neg_fib.append(c)

neg_fib.reverse()

print(f"{neg_fib, 0, pos_fib}")