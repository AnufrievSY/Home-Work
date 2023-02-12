"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.

Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив
данных,

b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться
сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random


def sorting(a):
    n = 1
    while n < len(a):
        old_array = a.copy()
        for i in range(len(a) - n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        if old_array == a:
            break
        else:
            n += 1
    print(f'\nСортировка выполненна за {n} циклов\n')
    return a


array = [i for i in range(-100, 100)]
random.shuffle(array)
print(f'Изначальный список: {array}')
print(f'Отсортированный список: {sorting(array)}')
