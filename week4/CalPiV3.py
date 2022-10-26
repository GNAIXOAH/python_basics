from random import random, seed
DARTS =eval(input())
hits = 0.0
seed(123)
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("{:.6f}".format(pi))