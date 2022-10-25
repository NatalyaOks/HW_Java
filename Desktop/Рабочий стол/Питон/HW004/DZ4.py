'''4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

*Пример:* 
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0''' 

from random import randint


k = int(input('Введите натуральную степень k: '))
koef = [randint(0, 100) for i in range(k)]
print(koef)
expr = ' + '.join([f'{(j,"")[j == 1]} X^ {i}' for i, j in enumerate(koef) if j][::-1])
expr = expr.replace('X^0', '')
expr = (expr, expr[:-2]) [expr[-2:] == '']
expr += " = 0"
print(expr)

with open('DZ4.txt', 'w') as data:
    data.write(expr)