from euler import sieve_eratosthenes
from math import sqrt


primes = sieve_eratosthenes(10**5)

def is_prime(n):
    lim = int(sqrt(n))
    for p in primes:
        if p > lim:
            break
        elif n%p==0:
            return False
    return True

if __name__ == '__main__':
    d = 1
    p = 0
    for s in range(3, 100000, 2):
        t = s**2
        d += 4
        for i in range(3):
            t -= s-1
            if is_prime(t):
                p += 1
        print('p/d = %.4f' % (p/d))
        if p/d < 0.1:
            print('Ans: %d' % s)
            break
