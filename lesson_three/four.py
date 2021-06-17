"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = [[],
          [],
          [],
          []]

for i in range(4):
    for g in range(4):
        matrix[i].append(int(input(f"{matrix[i]}: ")))
    print(matrix)


for i in matrix:
    sum_line = 0
    for g in i:
        sum_line += g
    matrix[i].append(sum_line)

print(matrix)