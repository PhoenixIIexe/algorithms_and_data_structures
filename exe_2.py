"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""


from random import uniform

def merge_sort(list_: list) -> list:
    if len(list_) <= 1:
        return list_

    left_list = merge_sort(list_[:len(list_) // 2])
    right_list = merge_sort(list_[len(list_) // 2:])
    left_index, right_index = 0, 0

    while len(left_list) > left_index and len(right_list) > right_index:
        if left_list[left_index] < right_list[right_index]:
            list_[left_index + right_index] = left_list[left_index]
            left_index += 1
        else:
            list_[left_index + right_index] = right_list[right_index]
            right_index += 1

    while len(left_list) > left_index:
        list_[left_index + right_index] =  left_list[left_index]
        left_index += 1
    while len(right_list) > right_index:
        list_[left_index + right_index] = right_list[right_index]
        right_index += 1

    return list_


main_list = [uniform(0, 50) for _ in range(11)]
print(main_list)

print(merge_sort(main_list))