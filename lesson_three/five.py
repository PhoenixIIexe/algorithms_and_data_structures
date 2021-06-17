"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

matrix = [[],
          [],
          [],
          []]

for i in range(4):
    for g in range(4):
        matrix[i].append(randint(0, 100))
print(matrix)


max_min_line = 0

for i in matrix:
    min_line = i[0]
    for g in i[1:]:
        if g < min_line:
            min_line = g
    if min_line > max_min_line:
        max_min_line = min_line

print(max_min_line)