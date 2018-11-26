from random import randint

l = [randint(-10, 10) for _ in range(10)]
for n in l:
    print(n+1)

s = input('Введите строку: ')
for letter in s:
    print(letter)
