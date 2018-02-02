import numpy as np

n=int(input())
if n % 2 == 0:
    x = ((n*n) / 48)
    print(int(np.ceil(x)))
else:
    y=(((n + 3) ^ 2) / 48)
    print(int(np.ceil(y)))
