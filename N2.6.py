num = int(input('Сколько вы хотите внести товаров: '))
data = [(input('Введите название товара, его цену, количество и единицу измерения через пробел: ')) for i in range(num)]

structura = []
num = 1
tovary = {"название": [], "цена": [], "количество": [], "единица измерения": []}

for each in data:
    each_new = each.split(' ')
    each_new[1] = int(each_new[1])
    each_new[2] = int(each_new[2])
    structura.append(tuple((num, {"название": each_new[0], "цена": each_new[1], "количество": each_new[2], "единица измерения": each_new[3]})))
    num += 1
print(structura)

for each in data:
    each_new = each.split(' ')
    each_new[1] = int(each_new[1])
    each_new[2] = int(each_new[2])
    tovary["название"].append(each_new[0])
    tovary["цена"].append(each_new[1])
    tovary["количество"].append(each_new[2])
    tovary["единица измерения"].append(each_new[3])
print(tovary)



