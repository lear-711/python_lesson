v = float(input('Введите значение выручки: '))
i = float(input('Введите значение издержек: '))

if v > i:
    print("Прибыль")
    r = float((v-i)/v)
    s = int(input('Введите количество сотрудников: '))
    pr = float((v-i)/s)
    print("Рентабельность =", r)
    print("Прибыль на одного сотрудника = ", pr)
if i > v:
    print("Убыток")