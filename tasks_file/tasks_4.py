"""Задание 4-1. Напишите простой калькулятор. Сосчитать и напечатать результат операции"""

s = input().split()
print(s)

if s[1] == '+':
    print(f"{s[0]} + {s[2]} = ", int(s[0]) + int(s[2]))
elif s[1] == '-':
    print(f"{s[0]} - {s[2]} = ", int(s[0])-int(s[2]))
elif s[1] == '*':
    print(f"{s[0]} * {s[2]} = ", int(s[0])*int(s[2]))
elif s[1] == '/':
    print(f"{s[0]} / {s[2]} = ", int(s[0])/int(s[2]))
else:
    print('Некорректный ввод')

# альтернативный вариант
eval("1 + 2")
eval(input())

"""Задание 4-2. Вводим натуральное число  n. Напечатайте спираль из чисел 1,2,3...n*n"""
n = int(input())
d = {}

for i in range(n):
    for j in range(n):
        d[i,j] = 0
for i in range(n):
    for j in range(n):
        print(d[i,j], end=' ')
    print()

print(d)

"""Задание 4-3. 2 предложения (содержат предложения и знаки припенания) определаить являются ли эти 
предложения анаграммами(имееют одинаковый набор букв) Игнорируем знаки препинания цифры и тд. 
Вывод true/false"""

s1 = input().split()
s2 = input().split()

dict1 = {}
dict2 = {}

print(type(s1[0]))

for i in s1:
    if type(i) != str:
        continue
    if i not in dict1:
        dict1[i] = 0
    dict1[i] += 1
print(dict1)




