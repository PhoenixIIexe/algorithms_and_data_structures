"""
1.Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
"""


from random import randint

def bubble_sort(list_: list) -> list:
    N = len(list_)
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if list_[j] < list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]

    return list_


main_list = [randint(-100, 100) for _ in range(10)]
print(main_list)

print(bubble_sort(main_list))