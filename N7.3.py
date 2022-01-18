
class Cell:

    def __init__(self, units):
        self.units = units

    def __add__(self, other):
        result = self.units + other.units
        return Cell(result)

    def __sub__(self, other):
        if self.units > other.units:
            result = self.units - other.units
            return Cell(result)
        else:
            return 'Невозможно выполнить операцию'

    def __mul__(self, other):
        result = self.units * other.units
        return Cell(result)

    def __truediv__(self, other):
        result = self.units // other.units
        return Cell(result)

    def make_order(self, rows):
        result1 = self.units // rows
        result2 = self.units % rows
        result = ''
        for i in range(result1):
            result += '*' * rows + '\n'
        if result2 != 0:
            result += '*' * result2
        return result


a = Cell(16)
b = Cell(5)

c = a + b
d = a - b
f = a * b
e = a / b

print(c.units)
print(d.units)
print(f.units)
print(e.units)
print(a.make_order(5))


