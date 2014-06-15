from euler import timeit


def isqrt(n):
    """ Newtons method
    returns the largest integer x for which x*x <= n
    """
    x, y = n, n+1
    while x < y:
        x, y = (x + n//x)//2, x
    # return the value of x before direction of tangent changed
    return y


def is_integer_squared(n):
    if isqrt(n)**2 == n:
        return True
    else:
        return False


@timeit
def solve(lim):
    res = 0
    val = 0
    for D in range(2, lim + 1):
        if not is_integer_squared(D):
            x, y = chakravala(D)
            if x > val:
                res = D
                val = x
    print('PE66 Ans: %d' % res)


def chakravala(D, verbose=0):
    """
    Resources
        [1] http://jwb.io/20121231-the-euclidean-algorithm-and-chakravala-method-in-ruby.html
        [2] http://cs.annauniv.edu/insight/Reading/algebra/indet/chakra.htm
    """
    p, k, x, y = 1, 1, 1, 0
    sq = round(D**0.5)

    # if verbose print table
    if verbose:
        i = 0 # iteration number
        print('Chakravala vidhi: x**2 - %d*(y**2) = 1' % (D))
        print(' r    p    k    x    y')
        print('%2d %4d %4d %4d %4d' % (i, p, k, x, y))

    while k!=1 or y==0:
        # choose p1 such that 
        #   1) p + p1 is divisible by k
        #   2) abs(p1*p1 - D) is minimum
        p1 = sq
        k_abs = abs(k)
        off = (p + p1) % k_abs
        if off:
            p1 = p1 - off
            if p1 < 1:
                p1 = p1 + k_abs
            elif abs(p1 - sq) < abs(p1 + k_abs - sq):
                pass
            else:
                p1 = p1 + k_abs

        # update equations for chakravala
        x, y, k = (x*p1 + D*y) // k_abs, (x + y*p1) // k_abs, (p1**2 - D) // k
        p = p1

        if verbose:
            i += 1
            print('%2d %4d %4d %4d %4d' % (i, p, k, x, y))

    return int(x), int(y)


def check(lim):
    cnt = 0
    for D in range(1, lim+1):
        if isqrt(D)**2 != D:
            x, y = chakravala(D)
            # x, y = int(x), int(y)
            tmp = x**2 - (D*(y**2))
            if tmp != 1:
                cnt += 1
                print(D)
    print('%d errors' % cnt)


if __name__ == '__main__':
    print(chakravala(2, verbose=1))
    print(chakravala(3, verbose=1))
    print(chakravala(5, verbose=1))
    print(chakravala(6, verbose=1))
    print(chakravala(7, verbose=1))
    print(chakravala(8, verbose=1))
    print(chakravala(61, verbose=1))
    print(isqrt(2), is_integer_squared(2))
    print(isqrt(24), is_integer_squared(24))
    print(isqrt(25), is_integer_squared(25))
    print(isqrt(26), is_integer_squared(26))
    solve(1000)
    check(1000)
    check(100000)
    # solve(10000)
