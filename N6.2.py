
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self, massa_na_metr, cm):
        res = self._length * self._width * massa_na_metr * cm
        return res


mkad = Road(100, 5)

r1 = mkad.massa(20, 10)
r2 = mkad.massa(30, 7)
print(r1, r2)

