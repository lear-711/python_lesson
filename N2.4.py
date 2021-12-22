stroka = str(input('Введите строку, разделяя слова пробелами: '))
stroka_new = stroka.split(' ')
num = 1

for word in stroka_new:
    if len(word) <= 10:
        print(num, ':', word)
    else:
        print(num, ':', word[:10])
    num += 1
