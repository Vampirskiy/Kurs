from random import randint
a = [2, 41, 5, 54, 96, 23, 91, 4, 10, 25]
b = []
b = [randint(1, 100) for i in b if len(b) < 11]
print(b)
def sravb(a):
    c = []
    n = 1
    for i in a:
        if n <= (len(a) - 1) and a[n] > a[n - 1]:
            c.append(a[n])
            n += 1
            continue
        else:
            n += 1
            continue
    return c

print(sravb(a))

