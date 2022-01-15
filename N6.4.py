
class Car:

    speed = 200
    color = 'Red'
    name = 'Lamborghini'
    is_police = False

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'текущая скорость: {self.speed}'

class TownCar(Car):

    def __init__(self, speed, name, color):
        self.speed = speed
        self.name = name
        self.color = color

    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости на {self.speed - 60}'
        else:
            return 'Вы соблюдаете скоростной режим!'

class SportCar(Car):

    def __init__(self, speed, name):
        self.speed = speed
        self.name = name


class WorkCar(Car):

    def __init__(self, speed, name, color):
        self.speed = speed
        self.name = name
        self.color = color

    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости на {self.speed - 40} км/ч'
        else:
            return 'Вы соблюдаете скоростной режим!'

class PoliceCar(Car):

    def __init__(self, color, is_police):
        self.color = color
        self.is_police = is_police


polo = TownCar(58, 'V_polo', 'white')
print(polo.name, polo.speed, polo.color, polo.is_police)
print(polo.show_speed(), '\n')

ferrari = SportCar(350, 'Ferrari')
print(ferrari.name, ferrari.speed, ferrari.color, ferrari.is_police, '\n')

largus = WorkCar(48, 'Lada_largus', 'black')
print(largus.name, largus.speed, largus.color, largus.is_police)
print(largus.show_speed(), '\n')

camry = PoliceCar('blue', True)
print(camry.name, camry.speed, camry.color, camry.is_police)
