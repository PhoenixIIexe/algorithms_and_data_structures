"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint
from sys import getsizeof


def show(obj):
    print(f'{type(obj)=}, {getsizeof(obj)},{obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'item'):
            for key, val in obj.items():
                show(key)
                show(val)
        else:
            for item in obj:
                show(item)


list_ = [randint(1, 99) for _ in range(10)]
print(list_)

print(f"Первоначальный массив: ")
show(list_)


def var_one(local_list):
    local_list = list(local_list)

    max_index = 0
    min_index = 0

    for i in range(1, len(local_list)):
        if local_list[i] > local_list[max_index]:
            max_index = i
        if local_list[i] < local_list[min_index]:
            min_index = i

    local_list[max_index], local_list[min_index] = local_list[min_index], local_list[max_index]
    print(local_list)

    print(f"""
Вариант номер один: 
max_index - {type(max_index)=}, {getsizeof(max_index)},{max_index=}
min_index - {type(min_index)=}, {getsizeof(min_index)},{min_index=}
i - {type(i)=}, {getsizeof(i)},{i=}
local_list:
    """)
    show(local_list)



def var_two(local_list):
    local_list = list(local_list)

    max_index = local_list.index(max(local_list))
    min_index = local_list.index(min(local_list))

    local_list[max_index], local_list[min_index] = local_list[min_index], local_list[max_index]
    print(local_list)

    print(f"""
Вариант номер два: 
max_index - {type(max_index)=}, {getsizeof(max_index)},{max_index=}
min_index - {type(min_index)=}, {getsizeof(min_index)},{min_index=}
local_list: 
    """)
    show(local_list)


def var_three(local_list):
    local_list = list(local_list)

    local_list = [{min(local_list): max(local_list), max(local_list): min(local_list)}.get(x, x) for x in local_list]
    print(local_list)

    print(f"""
Вариант номер три: 
local_list: 
    """)
    show(local_list)

var_one(list_)
var_two(list_)
var_three(list_)

"""
Итог:

[94, 94, 26, 44, 26, 22, 50, 66, 93, 49]
Первоначальный массив: 
type(obj)=<class 'list'>, 184,obj=[94, 94, 26, 44, 26, 22, 50, 66, 93, 49]
type(obj)=<class 'int'>, 28,obj=94
type(obj)=<class 'int'>, 28,obj=94
type(obj)=<class 'int'>, 28,obj=26
type(obj)=<class 'int'>, 28,obj=44
type(obj)=<class 'int'>, 28,obj=26
type(obj)=<class 'int'>, 28,obj=22
type(obj)=<class 'int'>, 28,obj=50
type(obj)=<class 'int'>, 28,obj=66
type(obj)=<class 'int'>, 28,obj=93
type(obj)=<class 'int'>, 28,obj=49
[22, 94, 26, 44, 26, 94, 50, 66, 93, 49]

Вариант номер один: 
max_index - type(max_index)=<class 'int'>, 24,max_index=0
min_index - type(min_index)=<class 'int'>, 28,min_index=5
i - type(i)=<class 'int'>, 28,i=9
local_list:
    
type(obj)=<class 'list'>, 136,obj=[22, 94, 26, 44, 26, 94, 50, 66, 93, 49]
type(obj)=<class 'int'>, 28,obj=22
type(obj)=<class 'int'>, 28,obj=94
type(obj)=<class 'int'>, 28,obj=26
type(obj)=<class 'int'>, 28,obj=44
type(obj)=<class 'int'>, 28,obj=26
type(obj)=<class 'int'>, 28,obj=94
type(obj)=<class 'int'>, 28,obj=50
type(obj)=<class 'int'>, 28,obj=66
type(obj)=<class 'int'>, 28,obj=93
type(obj)=<class 'int'>, 28,obj=49
[22, 94, 26, 44, 26, 94, 50, 66, 93, 49]

Вариант номер два: 
max_index - type(max_index)=<class 'int'>, 24,max_index=0
min_index - type(min_index)=<class 'int'>, 28,min_index=5
local_list: 
    
type(obj)=<class 'list'>, 136,obj=[22, 94, 26, 44, 26, 94, 50, 66, 93, 49]
type(obj)=<class 'int'>, 28,obj=22
type(obj)=<class 'int'>, 28,obj=94
type(obj)=<class 'int'>, 28,obj=26
type(obj)=<class 'int'>, 28,obj=44
type(obj)=<class 'int'>, 28,obj=26
type(obj)=<class 'int'>, 28,obj=94
type(obj)=<class 'int'>, 28,obj=50
type(obj)=<class 'int'>, 28,obj=66
type(obj)=<class 'int'>, 28,obj=93
type(obj)=<class 'int'>, 28,obj=49
[22, 22, 26, 44, 26, 94, 50, 66, 93, 49]

Вариант номер три: 
local_list: 
    
type(obj)=<class 'list'>, 184,obj=[22, 22, 26, 44, 26, 94, 50, 66, 93, 49]
type(obj)=<class 'int'>, 28,obj=22
type(obj)=<class 'int'>, 28,obj=22
type(obj)=<class 'int'>, 28,obj=26
type(obj)=<class 'int'>, 28,obj=44
type(obj)=<class 'int'>, 28,obj=26
type(obj)=<class 'int'>, 28,obj=94
type(obj)=<class 'int'>, 28,obj=50
type(obj)=<class 'int'>, 28,obj=66
type(obj)=<class 'int'>, 28,obj=93
type(obj)=<class 'int'>, 28,obj=49
"""