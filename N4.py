n = int(input('Введите целое положительное число: '))
n = str(n)

m = n[0]
i = 0

while i < len(n):
    if n[i] > m:
        m = n[i]
    i += 1

print(m)

