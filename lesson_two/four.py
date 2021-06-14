"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
чем то, что загадано.
"""

from random import randint

def main(a: int, i=1) -> int:
    if a == b:
        return 'Win'
    elif i == 10:
        return 'Lose'
    else:
        return main(int(input()), i+1)

b = randint(0, 100)

print(main(int(input())))