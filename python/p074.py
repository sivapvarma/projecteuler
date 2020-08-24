from math import factorial


def sum_of_digit_factorials(n):
    res = 0
    t = n
    while t:
        res, t = res + factorial(t%10), t//10
    return res


def chain_length(n):
    cnt = 0
    seen = set()
    sdf = n
    while not sdf in seen:
        cnt += 1
        seen.add(sdf)
        sdf = sum_of_digit_factorials(sdf)
    return cnt

def solve():
    lim = 10**6
    res = 0
    print(chain_length(69))
    for n in range(lim):
        if chain_length(n) == 60:
            res += 1
            # print('%d : %d' % (res, n))
    print('PE74 Ans: %d' % res)


if __name__ == '__main__':
    solve()
