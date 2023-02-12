"""
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним.
"""

a = input('Введите первое значение: ')
b = input('Введите второе значение: ')
c = input('Введите третье значение: ')

if a+b > c:
    if b+c > a:
        if a+c > b:
            print('Треугольник с такими сторонами может существовать')
            if a == b:
                if b == c:
                    if a == c:
                        print('Такой треугольник равносторонний')
                    else:
                        print('Такой треугольник равнобедренный')
                else:
                    print('Такой треугольник равнобедренный')
            elif b == c:
                print('Такой треугольник равнобедренный')
            elif a == c:
                print('Такой треугольник равнобедренный')
            else:
                print('Такой треугольник разносторонний')
        else:
            print('Треугольник с такими сторонами НЕ может существовать')
    else:
        print('Треугольник с такими сторонами НЕ может существовать')
else:
    print('Треугольник с такими сторонами НЕ может существовать')
