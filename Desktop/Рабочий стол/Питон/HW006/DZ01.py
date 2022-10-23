'''Задайте список из нескольких чисел. Напишите программу, которая 
найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, 
ответ: 12'''

# lst = [ 7, 8, 3, 5, 6]
# new_lst = []
# for i in range(len(lst)):
#     if i % 2 != 0:
#         new_lst.append(lst[i])
# print(new_lst)
# print(sum(new_lst))



lst = [ 2, 3, 5, 9, 3]
sum_n = 0
for i in enumerate(lst):
    if i[0] % 2 != 0:
        sum_n += i[1]
print(sum_n)
