import sys
from millerrabin import MillerRabin

f = file(sys.argv[1], "r")

matrix = [[c for c in l[:-1]] for l in f.readlines()]

x = len(matrix[0])
y = len(matrix)

def horizontal():
    for j in range(y):
        for i0 in range(x):
            for i1 in range(i0+1, x + 1):
                yield int("".join(matrix[j][i0:i1]))

def vertical():
    for i in range(x):
        for j0 in range(y):
            for j1 in range(j0+1, y + 1):
                yield int("".join(matrix[j][i] for j in range(j0, j1)))

primes = set()
for n in horizontal():
    if n > 1 and MillerRabin(n, 1000):
        primes.add(n)
for n in vertical():
    if n > 1 and MillerRabin(n, 1000):
        primes.add(n)

print sorted(primes)
print len(primes)
print max(primes)
