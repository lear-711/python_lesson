
with open('file.txt', 'r') as f:
    data = f.readlines()
    with open('new_rus_file.txt', 'w') as rf:
        dictionary = {
            'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре'
        }
        for lines in data:
            line = lines.split()
            line[0] = dictionary[line[0]]
            rf.write(' '.join(line) + '\n')

            # if line[0] == 'One':
            #     line[0] = 'Один'
            # elif line[0] == 'Two':
            #     line[0] = 'Два'
            # elif line[0] == 'Three':
            #     line[0] = 'Три'
            # elif line[0] == 'Four':
            #     line[0] = 'Четыре'
            # rf.write(' '.join(line) + '\n')


