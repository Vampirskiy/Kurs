a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = [i for i in a if a.count(i) == 1]
print(b)