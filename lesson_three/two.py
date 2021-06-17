"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

_list_ = [randint(1, 99) for _ in range(10)]
print(_list_)

max_index = 0
min_index = 0

for i in range(1, 10):
    if _list_[i] > _list_[max_index]:
        max_index = i
    if _list_[i] < _list_[min_index]:
        min_index = i

_list_[max_index], _list_[min_index] = _list_[min_index], _list_[max_index]
print(_list_)