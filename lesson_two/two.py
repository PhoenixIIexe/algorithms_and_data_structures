"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = input()
number_of_even_numbers = 0
number_of_odd_numbers = 0

for i in num:
    if int(i) % 2 == 0:
        number_of_even_numbers += 1
    elif int(i) % 2 == 1:
        number_of_odd_numbers += 1

print(f"""
Количество четных: {number_of_even_numbers}
Количество нечетных {number_of_odd_numbers}
""")