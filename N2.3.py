month = int(input('Введите номер в году вашего любимого месяца: '))
year = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

if month < 13:
    for key, value in year.items():
        if month in value:
            print(key, "- ваше любимое время года")
else: print('Введите число от 1 до 12!!')
