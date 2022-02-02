
class CheckDigits(ValueError):

    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    a = input('Введите число: ')
    if a == 'Stop':
        print(my_list)
        break
    try:
        try:
            a = float(a)
            my_list.append(a)

        except ValueError:
            raise CheckDigits('Проверь данные!')
    except CheckDigits as err:
        print(err)

