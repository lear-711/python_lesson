with open('subject.txt', 'r') as f:
    data = f.readlines()
    dictionary = {

    }

    for line in data:
        s = 0
        key, line = line.split(':')

        line1 = line.split()
        for i in line1:
            line2 = i.split('(')
            try:
                line2[0] = int(line2[0])
                s += line2[0]
            except:
                pass
        dictionary[key] = s
    print(dictionary)
