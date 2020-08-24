#!/usr/bin/python3
from euler import timeit
from math import sqrt


@timeit
def solve():
    lim = 1500000
    d = {}
    for m in range(2, int(sqrt(lim/2))):
        for n in range(1, m):
            a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
            a, b = min(a, b), max(a, b)
            p = a+b+c
            # print('%d  %d  %d -> %d <- %d, %d' % (a, b, c, p, m, n))
            ratio = 1
            for key in range(p, lim+1, p):
                sides = (ratio*a, ratio*b, ratio*c)
                if key not in d:
                    d[key] = [sides]
                else:
                    if not sides in d[key]:
                        d[key].append(sides)
                # scale the sides proportional to perimeter
                ratio += 1
    res = 0
    for k in d:
        if len(d[k]) == 1:
            res += 1
    print('PE75 Ans: %d' % res)



if __name__ == '__main__':
    solve()
