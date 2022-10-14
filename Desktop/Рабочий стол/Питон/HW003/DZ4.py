'''Напишите программу, которая будет преобразовывать десятичное 
число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

num = int(input('Введите число: '))
lst = []

while num >= 1:
    a = int(num % 2)
    lst.append(a)
    num = num / 2

lst.reverse()    

bin_ = ''
for i in lst:
    bin_ += str(i)
    
print(f'В двоичной системе число = {bin_}')
