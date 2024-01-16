
"""ЗАДАНИЕ 1. Ввести два числа: x и y. Напечатать наибольшее из этих чисел"""

x = int(input())
y = int(input())

if x >= y:
    print(x)
else:
    print(y)

"""ЗАДАНИЕ 2. Ввести два числа: x и y. Напечатать сумму и произведение этих чисел"""

x = int(input())
y = int(input())

sum = x + y
mult = x * y

print(sum, mult)

"""ЗАДАНИЕ 3. Ввести два числа: x и y. Напечатать наибольшее из чисел: x+y, x*y, x-y, x/y, x//y"""

# 1 решение
x = int(input())
y = int(input())

max_number = max(x+y, x*y, x-y, x/y, x//y)
print(max_number)

# 2 решение
x = int(input())
y = int(input())

max_number = x+y

if (x*y) > max_number:
    max_number = (x*y)
if (x-y) > max_number:
    max_number = (x-y)
if (x/y) > max_number:
    max_number = (x/y)
if (x//y) > max_number:
    max_number = (x//y)

print(max_number)

"""ЗАДАНИЕ 4. Ввести два числа: x и y. Напечатать второе наибольшее из чисел: x+y, x*y, x-y, x/y, x//y"""
x = int(input())
y = int(input())

nums = sorted([x+y, x*y, x-y, x/y, x//y])
print(nums[-2])
