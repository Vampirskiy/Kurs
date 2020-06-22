def fact(n):
    result, enumerate = 1
    number = 1
    for i in range(1, n):
        result *= i
        yield str(number) + '! = ' + str(result)
        number += 1
n = int(input('Введите число: '))
for el in fact(n + 1):
    print(el)



