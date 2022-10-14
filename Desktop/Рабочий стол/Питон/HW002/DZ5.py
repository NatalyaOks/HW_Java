'''Задание 5 Реализуйте алгоритм перемешивания списка.'''

from random import randint


lst = [1, 2, 3, 4, 5, 6, 7]
lst_new = []
for i in range(len(lst)):
        temp = randint(0, len(lst) - 1)
        lst_new.append(lst[temp])
        del lst[temp]
print(lst_new)

