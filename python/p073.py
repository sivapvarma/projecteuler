from fractions import gcd
from euler import timeit


@timeit
def solve(lim):
    res = 0
    for d in range(lim, 1, -1):
        for n in range((d)//3 + 1, (d-1)//2 + 1):
            if gcd(n, d) == 1:
                res += 1
                # print('%d / %d' % (n, d))
    print('PE73 Ans: %d' % res)


if __name__ == '__main__':
    solve(12000)
    
