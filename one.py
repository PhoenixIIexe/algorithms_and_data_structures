num = int(input())

print(f'Произведение {(num % 10) * (num // 10 % 10) * (num // 100 % 10)}')
print(f'Сумма {num % 10 + num // 10 % 10 + num // 100 % 10}')