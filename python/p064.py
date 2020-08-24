def periodr(a, b, c, b0):
    if c==1 and b == b0:
        return 0
    else:
        cn = (a - (b**2))//c
        q = (-b0-b)//cn
        bn = -b-(cn*q)
        return 1 + periodr(a, bn, cn, b0)

def period(n):
    a = n
    c = 1
    b = -isqrt(a)
    b0 = b
    # print('a=%d b=%d c=%d b0=%d' % (a, b, c, b0))
    cn = (a - (b**2))//c
    q = (-b0-b)//cn
    bn = -b-(cn*q)
    # print('a=%d bn=%d cn=%d b0=%d' % (a, bn, cn, b0))
    return 1 + periodr(a, bn, cn, b0)

def isqrt(n):
    y, x = n, n+1
    while y < x:
        x = y
        y = (x + n//x)//2
    return x

if __name__ == '__main__':
    cnt = 0
    for n in range(2, 10001):
        if isqrt(n)**2 != n and period(n)%2==1:
                cnt += 1
    print(cnt)



