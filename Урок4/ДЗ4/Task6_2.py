from itertools import cycle
import sys
sys.argv
def vivod(a):
    n = 1
    for i in cycle(a):
        if n > 10:
            break
        print(i)
        n += 1
try:
    a = sys.argv[1]
except Exception:
    print('Необходимо ввести набор значений!')
else:
    vivod(a)