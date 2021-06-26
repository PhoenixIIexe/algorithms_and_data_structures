"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""


from collections import namedtuple
from random import randint, uniform

avg_all_comp_total = 0
all_comp = []
Comp = namedtuple('Comp', 'name, p1, p2, p3, p4, total')
number_of_comp = randint(0, 10)
for _ in range(number_of_comp):
    name = randint(0, 10)
    p_serial = []
    total = 0
   
    for __ in range(4):
        profit = uniform(0, 1000)
        p_serial.append(profit)

    total = sum(p_serial)
    avg_all_comp_total += sum(p_serial)
    all_comp.append(Comp(name, *p_serial, total))

avg_all_comp_total /= number_of_comp

print('Предприятия, у которых прибыль выше среднего:')
for comp in all_comp:
    if comp.total > avg_all_comp_total:
        print(f'{comp.name} - {comp.total}')

print('Предприятия, у которых прибыль ниже среднего:')
for comp in all_comp:
    if comp.total < avg_all_comp_total:
        print(f'{comp.name} - {comp.total}')