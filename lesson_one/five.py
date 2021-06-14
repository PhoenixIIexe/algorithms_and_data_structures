first_segment = int(input("Первый отрезок: "))
second_segment = int(input("Второй отрезок: "))
third_segment = int(input("Второй отрезок: "))

if abs(second_segment - third_segment) < first_segment < second_segment + third_segment and abs(first_segment - third_segment) < second_segment < first_segment + third_segment and abs(first_segment - second_segment) < third_segment < first_segment + second_segment:
    if first_segment == second_segment == third_segment:
        print('Треугольник равносторонний')
    elif first_segment == second_segment or first_segment == third_segment or second_segment == third_segment:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольника не существует')