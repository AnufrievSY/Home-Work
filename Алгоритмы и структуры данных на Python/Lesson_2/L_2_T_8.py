"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

quantity = input('Сколько чисел вы собираетесь ввести: ')
find = (input('Какое число необходимо искать: '))

answer_1 = 0

for j in range(int(quantity)):
    value = input(f'Ввод (число {j+1}): ')
    for i in value:
        if i == find:
            answer_1 += 1

print(f'В введенных вами {quantity} чисел, {find} встречается {answer_1} раз.')

