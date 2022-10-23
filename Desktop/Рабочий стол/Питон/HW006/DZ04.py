'''Задание 2 Напишите программу, которая принимает на вход число N и 
выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

# n = int(input('Введите число: '))
# product = 1
# lst = []
# for i in range(n):
#     product *= i + 1
#     lst.append(product)
# print(lst)

import math
 
n = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * math.factorial(x - 1)
lst = list(f(i) for i in range(1, n + 1))
print(lst)