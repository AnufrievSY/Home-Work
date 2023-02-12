"""
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

a = 5
b = 6

print(f'Число 1 = {a}')
print(f'Число 2 = {b}')

print(f'Побитовое "ИЛИ": {a | b}')
print(f'Исключающее "ИЛИ": {a ^ b}')
print(f'Побитовое "И": {a & b}')
print(f'Побитовое отрицание {a}: {~a}')
print(f'Побитовое отрицание {b}: {~b}')
print(f'Побитовый сдвиг числа {a} вправо на два 2 знака: {a >> 2}')
print(f'Побитовый сдвиг числа {a} влево на два 2 знака: {a << 2}')
