
with open('data.txt', 'r') as f:
    data = f.readlines()
    st = 0
    for stroka in data:
        st += 1
        sl = len(stroka.split())
        print (f'Количество слов в строке {st}: {sl}')
    print(f'Количество строк: {st}')