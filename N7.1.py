
class Matrix:

    def __init__(self, matrica):
        self.matrica = matrica
        self.formated_matrica = ''
        for i in matrica:
            self.formated_matrica += ' '.join([str(_) for _ in i]) + '\n'

    def __str__(self):
        return self.formated_matrica

    def __add__(self, other):
        result = []
        for i in range(len(self.matrica)):
            result.append([0] * len(self.matrica[i]))
            for j in range(len(self.matrica[i])):
                result[i][j] = self.matrica[i][j] + other.matrica[i][j]
        return Matrix(result)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Матрица a: \n{a}')

b = Matrix([[3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(f'Матрица b: \n{b}')

n = a + b
print(f'Результат сложения матриц а и b: \n{n}')


