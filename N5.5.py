from random import randint

my_list = [randint(0, 100) for _ in range(10)]

with open('summa.txt', 'w') as f:
    for each in my_list:
        each = str(each)
        f.write(each + ' ')
with open('summa.txt', 'r') as rf:
    data = [int(each) for each in rf.read().split()]
    print(sum(data))

