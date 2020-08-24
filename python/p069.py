from euler import sieve_eratosthenes

primes = []

def euler_totient(n):
    prime_factors = []
    # if n is primes - n-1 relatively primes before it
    if n in primes:
        return n-1
    for p in primes:
        if p > n:
            break
        elif n%p == 0:
            prime_factors.append(p)
    phi = n
    for p in prime_factors:
        phi = (phi*(p-1))//p
    return phi

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


def main():
    lim = 10**6
    global primes
    primes = sieve_eratosthenes(lim)
    val = 0
    res = 1
    for n in range(2, lim+1):
        print(n)
        tmp = n / euler_totient(n)
        if tmp > val:
            val = tmp
            res = n
    print('Ans: %d' % res)


def solve():
    lim = 10**6
    phi = sieve_totient(lim)
    val = 0
    res = 1
    for n in range(2, lim+1):
        tmp = n / phi[n]
        if tmp > val:
            val = tmp
            res = n
    print('Ans: %d' % res)


if __name__ == '__main__':
    solve()
