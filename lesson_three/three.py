"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

from random import randint

_list_ = [randint(0, 100) for _ in range(10)]
print(_list_)

min_one = 101
min_two = 101

for i in _list_:
    if i <= min_one:
        min_two = min_one
        min_one = i

print(min_one, min_two)