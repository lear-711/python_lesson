x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

def vozved_v_stepen(x, y):
    x1 = 1
    y = abs(y)
    for i in range(y):
        x1 *= x
    res = 1/x1
    return(res)

print(vozved_v_stepen(x, y))

#Второе решение

x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

def vozved_v_stepen_simple(x, y):
    return x**y

print(vozved_v_stepen_simple(x, y))