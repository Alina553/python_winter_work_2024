""""Задача 1 . ввести число  n. Вывести треугольник паскаля"""

lst = [[1]]
n = int(input())

for i in range(1, n):
    cur = [1]
    for j in range(1,i):
        cur.append(lst[-1][j-1] + lst[-1][j])
    cur.append(1)
    lst.append(cur)
for cur in lst:
    print(*cur)  #печать без скобок

"""Задача 2. ввести число. вывести все его делители"""

n= int(input())

for i in range(1, n+1):
    if n%i == 0:
        print(i,end=' ')

"""более сложный вариант, если хотим узнатть сколько раз делится на 3/3 и тп то используем словарь
напечатать простые делите"""

n= int(input())
dc = {}

for i in range(2, n+1):
    while n % i == 0:  #опеределяем делители
        dc[i] = dc.get(i, 0) + 1  # прирасщиваем словарь если i есть в словаре то добавим 1, если нет то 0
        n = n // i
print(dc)


"""адание 3, напечатайте ряд фибоначчи до введенного номера n"""

n = int(input())
a, b = 0, 1

for i in range(n):
    print(b, end= ' ')
    a, b = b, a + b

"""более сложная форма"""
for i in range(n):
    print(b, end= ' ')
    c = a
    a = b
    b = c + b