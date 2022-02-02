
class Store:

    storage = {}

    def fill(self, printers, scaners, xeroxs):
        self.storage['printers'] = printers
        self.storage['scaners'] = scaners
        self.storage['xeroxs'] = xeroxs

    def get(self, c_printers, c_scaners, c_xeroxs):
        res = {}
        res['printers'] = self.storage['printers'][:c_printers]
        res['scaners'] = self.storage['scaners'][:c_scaners]
        res['xeroxs'] = self.storage['xeroxs'][:c_xeroxs]
        return res


class OfficeEquipment:

    Energy = 50
    Year = 2015
    Manufacturer = 'HP'


class Printer(OfficeEquipment):

    def __init__(self, colors):
        self.colors = colors


class Scaner(OfficeEquipment):

    def  __init__(self, format):
        self.format = format


class Xerox(OfficeEquipment):

    def __init__(self, type, size):
        self.type = type
        self.size = size


class CheckValues(ValueError):

    def __init__(self, txt):
        self.txt = txt


color_printer = Printer(3)
bw_printer = Printer(1)

format_1_sc = Scaner('A3')
format_2_sc = Scaner('A4')

x1 = Xerox(3, 'Big')
x2 = Xerox(1, 'Small')

s = Store()
s.fill([color_printer, bw_printer], [format_1_sc, format_2_sc], [x1, x2])

a = input('Введите количество принтеров: ')
b = input('Введите количество сканеров: ')
c = input('Введите количество ксероксов: ')

try:
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        print(s.get(a, b, c))
    except ValueError:
        raise CheckValues('Проверь данные!')
except CheckValues as err:
    print(err)