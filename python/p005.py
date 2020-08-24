from euler import timeit, gcd


@timeit
def solve(lim):
    l = [i for i in range(1, lim + 1)]
    res = 1
    for n in l:
        if res % n != 0:
            res *= n//gcd(res, n)
    return res


if __name__ == "__main__":
    print("PE #5 Ans: ", solve(20))
