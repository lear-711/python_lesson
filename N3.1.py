
def deleniye():
    """Деление первого числа на второе"""
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число, отличное от нуля: '))
    if b == 0:
        print('Деление на 0 невозможно')
        b = float(input('Введите другое число, отличное от нуля!!! '))
        if b == 0:
            return 'Программа завершена!'
        else:
            return a / b
    else:
        return a/b

print(deleniye())
