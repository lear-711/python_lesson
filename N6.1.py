import time


class TrafficLight:
    __color = 'Красный'

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = 'Желтый'
        print(self.__color)
        time.sleep(2)
        self. __color = 'Зеленый'
        print(self.__color)
        time.sleep(5)


svetofor = TrafficLight()
svetofor.running()

