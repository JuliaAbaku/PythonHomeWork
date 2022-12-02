# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число '))
list1 = list(range(-n, n+1))
print (list1)

data = open('file.txt', 'w')
data.write('1\n')
data.write('3\n')
data.write('5')
data.close

path = 'file.txt'
data = open('file.txt', 'r')
a = 1
for line in data:
    i = int(line)
    print(f'элемент на позиции {i}: {list1[i]}')
    a = a*list1[i]
print(f'произведение элементов равно: {a}')

data.close