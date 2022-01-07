from itertools import count, cycle

a = int(input('Введите начальное число: '))
b = int(input('Введите конечное число: '))
for i in range(a, b+1):
    count()
    print(i)


my_list = [2, 'Hello', 345, 3.9, 'Python']
gener = cycle(my_list)
count = 0

for i in gener:
    if count == 20:
        break
    count += 1
    print(i)