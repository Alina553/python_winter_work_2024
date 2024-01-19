"""Оператор  for, строки, списки"""


"""Задание 1. Дан список чисел, создайте новый список, каждый элемент которого является суммо числе первого списка"""

lst = [1,2,3,4,5]
lst_new = []
sum = 0

for i in range(len(lst)):
    sum = sum + (i+1)
    lst_new.append(sum)
print(lst_new)

"""Задание 1-1. Дан список списков чисел. Сосчитайте сумму всех чисел всех подписков"""

lst = [[5,2,3],[10,20],[101]]
sum = 0
for j in range(len(lst)):
    new_lst = lst[j]
    for k in range(len(new_lst)):
        sum = sum + new_lst[k]
print(sum)

"""Задание 2. Введите число n. Напишите таблицу умножения для n"""

n = int(input())
for i in range(1,10):
    mult = n * i
    print(f"{n} * {i} = {mult}")


"""Задача 2-2. Введите список lst состоящий из цифр. Найдите и напечатайте наименьшее число из списка"""

lst = [0.01,3,2,0.5,4,-20]
min_number = lst[0]

for i in range(len(lst)):
    if lst[i] < min_number:
        min_number = lst[i]
print(min_number)

"""Задача 2-3. Введите число n. Сосчитайте и напечатайте факторила числа n"""

n = int(input())
num = 1
for i in range(1,n+1):
    num = num * i
print(num)