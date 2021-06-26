"""
2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def converting_to_decimal(number):
    decimal_num = 0

    for i, meaning in enumerate(number):
        if ord(meaning) >= 65:
            num = ord(meaning) - 55
        else:
            num = int(meaning)
        decimal_num += num * 16 ** i 
    
    return decimal_num

def converting_to_hexadecimal(number):
    last_num_sis = []

    while number != 0:
        g = number % 16
        if g > 9:
            last_num_sis.append(chr(g + 55))
        else:
            last_num_sis.append(str(number % 16))
        number = (number - g) // 16

    return ''.join(last_num_sis[::-1])


num_1 = deque(input("Введите первое число: ")[::-1])
num_2 = deque(input("Введите второе число: ")[::-1])

num_1 = converting_to_decimal(num_1)
num_2 = converting_to_decimal(num_2)

sum_ = num_1 + num_2
mul_ = num_1 * num_2


print(f"""
Сумма чисел из примера: {converting_to_hexadecimal(sum_)},
Произведение: {converting_to_hexadecimal(mul_)}
""")