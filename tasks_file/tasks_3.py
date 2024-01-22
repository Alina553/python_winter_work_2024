"""Практикак списки циклы for, while"""

"""Задание 1. Вводить в бесконечном цикле зарплаты сотрудников. Окончание ввода- ввод 0. Напечатать среднюю зп"""

count = 0
salary = 0
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
n = int(input())
s = str(n)

# преобразовываем число в строку
lst = []
for i in range(len(s)):
    lst.append(int(s[i]))

# вычисляем количество цифр в числе
for k  in range(len(lst)):
    number = lst.count(k)
    print(f'{k} - {number}')


"""Задача3-3. На вход подается предложение из нескольких слов. Слова разделены пробелами. Напечатайте первое самое длинное слово"""

s = input()

new_s = s.split()
print(new_s)

max_word = new_s[0]
for i in range(len(new_s)):
    if len(new_s[i]) > len(max_word):
        max_word = new_s[i]

print(max_word)

