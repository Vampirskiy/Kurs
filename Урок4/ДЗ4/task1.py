import sys
sys.argv
try:
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
except NameError:
    print('Введите выроботку: _  , введите ставку: _  , введите премию: _')
def zarplata(a, b, c):
        print((int(a) * int(b)) + int(c))
zarplata(a, b, c)