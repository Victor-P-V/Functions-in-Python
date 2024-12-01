def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('количество строк матрицы:'))
m = int(input('количество столбцов матрицы:'))
value = input('значения матрицы: ')
matrix = get_matrix(n, m, value)

if n <= 0:
    print("задано неверное количество строк:", n)
elif m <=0:
    print("задано неверное количество столбцов:" ,m)
else:
    for i in matrix:
        print(*i)


