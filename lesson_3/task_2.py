first_quarter = int(input('Введите сумму дохода первого квартала: '))
second_quarter = int(input('Введите сумму дохода второго квартала: '))
third_quarter = int(input('Введите сумму дохода третьего квартала: '))
fourth_quarter = int(input('Введите сумму дохода четвертого квартала: '))

result = (first_quarter + second_quarter) / (third_quarter + fourth_quarter)
print(result)
