num = int(input())

sums = num % 10 + num // 10 % 10 + num // 100 % 10
muls = (num % 10) * (num // 10 % 10) * (num // 100 % 10)

print(f'Произведение {muls}')
print(f'Сумма {sums}')