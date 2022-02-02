
class ComplexDigits:

    def __init__(self, base, complex):
        self.base = base
        self.complex = complex

    def __add__(self, other):
        return ComplexDigits(self.base + other.base, self.complex + other.complex)

    def __mul__(self, other):
        return ComplexDigits(self.base * other.base - self.complex * other.complex,
                             self.base * other.complex + self.complex * other.base)

    def __str__(self):
        return str(self.base) + ' + ' + str(self.complex) + 'i'


a = ComplexDigits(5, 2)
b = ComplexDigits(7, 1)

print(a + b)
print(a * b)