from euler import timeit


def pentagonal():
    k = 1
    while True:
        yield (k, (k*(3*k - 1))//2)
        yield (-k, (k*(3*k + 1))//2)
        k += 1

@timeit
def main():
    p = [1, 1]
    n = 2
    while True:
        t = 0
        for k, n0 in pentagonal():
            if n0 > n:
                break
            t += int((-1)**(k-1))*p[n-n0]

        p.append(t)
        if t % 1000000 == 0:
            print('p({}) = {}'.format(len(p)-1, t))
            break
        n += 1

    # for n, pn in enumerate(p):
    #     print('p({}) = {}'.format(n, pn))


@timeit
def solve_euler():
    p = [1, 1]
    N = 1000000
    n = 1
    while p[n] != 0:
        n += 1
        i = 0
        t = 0 # temp variable to accumulate p[n]
        while True:
            i += 1
            m1 = n - (i*(3*i - 1))//2
            m2 = n - (i*(3*i + 1))//2
            s = 1
            if i % 2 == 0: s = -1
            if m1 >= 0: t += s * p[m1]
            if m2 >= 0: t += s * p[m2]
            if m1 < 0 and m2 < 0:
                break
        t = t % N
        p.append(t)
    print('PE78 Ans: {}'.format(n))


if __name__ == '__main__':
    main()
    solve_euler()


# First try - wrong logic
# if __name__ == "__main__":
#     limit = 10**5
#     T = 10**6
#     partitions = [1]+[0]*limit
#     for k in range(1, limit+1):
#         for n in range(k, limit+1):
#             partitions[n] += partitions[n-k]
#         if partitions[k] % T == 0:
#             print("PE78 Ans: %d" % k)
#             break
