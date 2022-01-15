
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        return f'Доход с учетом премии = {total_income} миллионов долларов'


programmist = Position('Илон', 'Маск', 'Boss', 100000, 2000)
print(programmist.get_full_name())
print(programmist.get_total_income())
