
def summa(a):
    sum = 0
    for each in a:
        each = float(each)
        sum += each
    return(sum)


def loop_check_input():
    sum_total = 0
    while True:
        a = input('Введите строку чисел, разделенных пробелом: ')
        if "S" in a:
            a = a.split("S")[0].split( )
            sum_total += summa(a)
            return sum_total
        else:
            a = a.split()
            sum_total += summa(a)
        print(sum_total)

print(loop_check_input())




