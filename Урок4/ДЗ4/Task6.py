import sys
from itertools import count
sys.argv
def vivod(a):
    for i in count(a):
        if i > 20:
            break
        else:
            print(i)
try:
    a = int(sys.argv[1])
except Exception:
    print('Необходимо начальное число!')
else:
    vivod(a)
