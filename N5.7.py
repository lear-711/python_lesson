import json

with open('firmy.txt', 'r')as f:
    data = f.readlines()
    obs_pribyl = 0
    count = 0

    dict1 = {}
    dict2 = {}

    for line in data:
        line = line.split()
        profit = int(line[2])
        expence = int(line[3])
        dict1[line[0]] = profit - expence

        if profit > expence:
            obs_pribyl += profit - expence
            count += 1
    dict2['average_profit'] = obs_pribyl/count
    my_list = [dict1, dict2]

with open('new.json', 'w') as jf:
    json.dump(my_list, jf)
