''' Задайте последовательность чисел. Напишите программу, которая выведет список 
неповторяющихся элементов исходной последовательности.

*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]'''

lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
new_lst = []
lst.sort()
print(lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] == lst[j] and i != j: 
            break
    else:
        new_lst.append(lst[i])
print(new_lst)