'''Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и 
выведите на экран их сумму, округлённую до трёх знаков после точки.

Пример:
Для n = 6 -> 14.072'''

# n = int(input("Введите число N: "))
# lst = []

# for i in range(1, n + 1):
#     f = (1+1/i)**i
#     lst.append(f)
        
# print(round(sum(lst), 3))

n = int(input("Введите число N: "))
lst = list(i for i in range(1, n+1))
print(sum(map(lambda x: ((1+1/x)**x), lst)))