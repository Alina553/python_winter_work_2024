"""Практикак списки циклы for, while"""

"""Задание 1. Вводить в бесконечном цикле зарплаты сотрудников. Окончание ввода- ввод 0. Напечатать среднюю зп"""

count = 0 #счетчик
salary = 0 #кол-о сотрудников
while True:
    n = float(input())
    if n < 0 or n == 0:
        break
    salary = salary + n
    count += 1
    avr_salary = salary / count
print(count)
print(salary)
print(avr_salary)

"""Задача 3-2. Дано целое число. Сосчитай сколько его записи нулей, единиц и тд"""
# n = int(input())
# s = str(n)

# # преобразовываем число в строку
# lst = []
# for i in range(len(s)):
#     lst.append(int(s[i]))
#
# # вычисляем количество цифр в числе
# for k  in range(len(lst)):
#     number = lst.count(k)
#     print(f'{k} - {number}')

s = input()
for k in '0123456789':
    print(k, '-', s.count(k))

# решение №2
hm = [0] * 10
print(hm) #[0,0,0,0,0,0,0,0,0,0]

for k in s:
    i =  int(k)
    hm[i] += 1
print(hm)

# решение 3
for k, v in enumerate(hm):
    print(k, '-', v)

"""Задача3-3. На вход подается предложение из нескольких слов. Слова разделены пробелами. Напечатайте первое самое длинное слово"""

s = input()

new_s = s.split()
print(new_s)

max_word = new_s[0]
for i in range(len(new_s)):
    if len(new_s[i]) > len(max_word):
        max_word = new_s[i]

print(max_word)

# 2 решение
s = input().split()
ma = ''

for w in s:
    if len(w) > len(ma): # если будут два слова одинаковой длины, то при > выведет 1 словао, а при >= выведет последнее
        ma = w

for w in s:
    if len(w) == len(ma): #выведет все длинные слова с одинаковым кол-м букв
        print(w)

s=input().split()
res = ['']

for w in s:
    if len(w) == len(res[0]): #создаст новый список res из максимальных слов
        res.append(w)
    elif len(w) < len(res[0]):
        pass
    elif len(w) > len(res[0]):
        res = [w]