letter_one = input("Первая буква: ").lower()
letter_two = input("Вторая буква: ").lower()

print(f"""
Первая буква на месте {ord(letter_one)-96}
Вторая буква на месте {ord(letter_two)-96}
Между ними {abs(ord(letter_one) - ord(letter_two)) - 1}
""")