def sieve_totient(n):
    lim = n
    phi = [i for i in range(n+1)]
    is_prime = [True]*(n+1)
    for i in range(2, lim+1):
        if is_prime[i]:
            phi[i] = i-1
            for j in range(2*i, lim+1, i):
                is_prime[j] = False
                phi[j] = (phi[j]*(i-1))//i
    return phi


def solve():
    lim = 10**7
    phi = sieve_totient(lim)
    val = lim
    res = 1
    for n in range(2, lim+1):
        if (''.join(sorted(str(n)))) == (''.join(sorted(str(phi[n])))):
            tmp = n / phi[n]
            if tmp < val:
                val = tmp
                res = n
    print('Ans: %d' % res)


if __name__ == '__main__':
    solve()
