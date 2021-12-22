my_list = [7, 5, 3, 3, 2]
new_value = int(input('Введите натуральное число: '))
ind = 0

for each in my_list:
    if each < new_value:
        my_list.insert(ind, new_value)
        break
    ind += 1

print(my_list)
