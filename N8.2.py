
class NoDevizionZero(Exception):

    def __init__(self, txt):
        self.txt = txt


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

try:
    if b == 0:
        raise NoDevizionZero('Деление на ноль запрещено!')
    rez = a/b
    print(f'Результат деления: {rez}')
except NoDevizionZero as err:
    print(err)