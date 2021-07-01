"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""


from random import randint


def median(list_: list) -> int:
    """
    while len(list_) > 2:
        list_.remove(max(list_))
        list_.remove(min(list_))
    mediana = list_[0]

    return mediana
    """
    max_elements, min_elements = [list_[0]], [list_[0]]

    for i in range((len(list_)-1) // 2):
        for item in list_:
            if max_elements[i] < item and item not in max_elements:
                max_elements[i] = item
            elif min_elements[i] > item and item not in min_elements:
                min_elements[i] = item
        max_elements.append(min_elements[0])
        min_elements.append(max_elements[0])
        print(max_elements, min_elements)

    return list(set(list_) - set(max_elements[:-1]) - set(min_elements[:-1]))[0]


SIZE = randint(1, 5) * 2 + 1
main_list = [randint(-100, 100) for _ in range(SIZE)]
print(main_list)

print(median(main_list))