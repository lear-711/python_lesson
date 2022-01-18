from abc import ABC, abstractmethod

class Clothes:

    @property
    @abstractmethod
    def calculation(self):
        pass

    # def __init__(self, name, size):
    #     self.name = name
    #     self.size = size
    #
    # def calculation(self):
    #     if self.name == 'Пальто':
    #         return self.size/6.5 + 0.5
    #     else:
    #         return self.size*2 + 0.3

class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def calculation(self):
       return self.size/6.5 + 0.5

class Suit(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def calculation(self):
        return self.size * 2 + 0.3


coat = Coat(54)
suit = Suit(1.8)
print(f'Расход ткани на пальто = {coat.calculation:.3f} м')
print(f'Расход ткани на костюм = {suit.calculation} м')
