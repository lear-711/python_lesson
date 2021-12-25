a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

def my_func(a, b, c):
    """Вывод суммы наибольших двух аргументов"""
    if (a > c) and (b > c):
        return a + b
    if (a > b) and (c > b):
        return a + c
    if (b > a) and (c > a):
        return c + b
    else:
        return 'Невозможно посчитать сумму наибольших двух аргументов'

print(my_func(a, b, c))