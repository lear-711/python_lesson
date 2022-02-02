
class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def my_method(cls, date):
        date = date.split('-')
        my_list = [int(i) for i in date]
        return my_list

    @staticmethod
    def validation(my_list):
        if (my_list[0] > 0) and (my_list[0] < 32) \
                and (my_list[1] > 0) and (my_list[1] < 13) \
                and my_list[2] < 2023:
            print('Валидация прошла успешно!')
        else:
            print('Валидация не пройдена!')


ex = Data('13-04-1778')
my_list = ex.my_method(ex.date)

ex.validation(my_list)
