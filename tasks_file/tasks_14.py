"""Задача 14-1
• Напишите рекурсивную функцию, которая вычисляет количество
цифр введенного целого числа n (n >= 0)."""

def func(n):
    if len(str(n)) == 1:
        return 1
    else:
        return len(str(n))

print(func(123456))

"""Задача 14-2
• Напишите рекурсивную функцию, которая вычисляет сумму цифр целого числа n (n >= 0)."""

def func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        s = [symbol for symbol in str(n)]
        dig = list(map(int,s))

        sum = 0
        for i in dig:
            sum += i

        return sum

print(func(1234))

"""Задача 14-3
Напишите рекурсивную функцию tri_2(n), которая печатает два треугольника. Например, для n = 5:"""

def func(n):
    print('*' * n)
    n -= 1
    if n > 0:
        func(n)
    print('*' * (n+1))
    return
func(6)
