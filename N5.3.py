
with open('salary.txt', 'r') as f:
    data = f.readlines()
    summa = 0
    st = 0
    for i in data:
        name, sal = i.split()
        sal = int(sal)
        summa += sal
        st += 1
        if sal > 20000:
            print(name)
    print(f'Средняя величина дохода сотрудников = {summa/st} рублей')