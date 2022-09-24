'''Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
всех значений предикат.'''

from operator import truediv
from turtle import right


def is_True (X, Y, Z):
    leftPart = not (X or Y or Z)
    rightPart = not X and not Y and not Z
    if leftPart == rightPart:
        return True
    else:
        return False

if is_True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')

