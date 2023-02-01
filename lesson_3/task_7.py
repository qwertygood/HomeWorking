number = int(input('Введите четырехзначное число: '))

a = number % 10
b = number % 100 // 10
c = number // 100 % 10
d = number // 1000
print(d, c, b, a)
