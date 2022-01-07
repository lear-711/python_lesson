
def fact(n):
    a = 1
    if n == 0:
        yield(a)
    for i in range(1, n+1):
        a *= i
        yield(a)

n = 6
for el in fact(n):
    print(el)
