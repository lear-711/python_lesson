
class Stationery:

    title = 'Канцелярская принадлежность'

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Подписываем рисунок'


class Pencil(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Рисуем контуры'


class Handle(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Раскрашиваем рисунок'


ruchka = Pen('Ручка')
print(ruchka.title + ':')
print(ruchka.draw(), '\n')

karandash = Pencil('Карандаш')
print(karandash.title + ':')
print(karandash.draw(), '\n')

marker = Handle('Маркер')
print(marker.title + ':')
print(marker.draw())

