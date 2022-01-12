
with open('new_file.txt', 'a+') as f:
    while True:
        s = input('Введите строку с данными: ')
        if s == '':
            break
        else:
            f.write(s + '\n')
    f.seek(0)
    data = f.read()
    print(data)
