spisok = input('Введите несколько элементов через пробел: ')
spisok_new = spisok.split(' ')
ind = 0

while ind < (len(spisok_new)-1):
    spisok_new[ind], spisok_new[ind + 1] = spisok_new[ind + 1], spisok_new[ind]
    ind += 2

print(spisok_new)

