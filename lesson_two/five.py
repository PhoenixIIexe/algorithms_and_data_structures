"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

def sum_of_digits(num, sum=0):
    if num == 0:
        return sum
    else:
        return sum_of_digits(num//10, sum + num % 10)

_max_ = 0

while True:
    num = int(input())
    if num == 0:
        break
    if _max_ < sum_of_digits(num):
        num_max = num
        _max_ = sum_of_digits(num)

print(f"Число: {num_max}\nСумма его цифр: {_max_}")