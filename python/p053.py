from fractions import Fraction
from operator import mul
from functools import reduce


def nCk(n, k):
    """ returns number of combinations of k out of n different items
    Source: http://stackoverflow.com/a/3027128/1034279
    """
    return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))

if __name__ == '__main__':
    cnt = 0
    n = 23
    mil = 10**6
    nu = 100
    while n <= nu:
        r = 3
        while nCk(n, r) <= mil:
            r += 1
        cnt += n+1-(2*r)
        n += 1
    print(cnt)
