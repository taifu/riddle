import sys
import random

def toBinary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
    return r

def test(a, n):
    """
    test(a, n) -> bool Tests whether n is complex.

    Returns:
        - True, if n is complex.
        - False, if n is probably prime.
    """
    b = toBinary(n - 1)
    d = 1
    for i in xrange(len(b) - 1, -1, -1):
        x = d
        d = (d * d) % n
        if d == 1 and x != 1 and x != n - 1:
            return True # Complex
        if b[i] == 1:
            d = (d * a) % n
    if d != 1:
        return True # Complex
    return False # Prime
    
def MillerRabin(n, s = 50):
    """
    MillerRabin(n, s = 50) -> bool Checks whether n is prime or not

    Returns:
        - True, if n is probably prime.
        - False, if n is complex.
    """
    for j in xrange(1, s + 1):
        a = random.randint(1, n - 1)
        if (test(a, n)):
            return False # n is complex
    return True # n is prime
    
def main(argv):
    if len(argv) > 2:
        print MillerRabin(int(argv[0]), int(argv[1]))
    else:
        print MillerRabin(int(argv[0]))
    
if __name__ == "__main__":
    main(sys.argv[1:])
