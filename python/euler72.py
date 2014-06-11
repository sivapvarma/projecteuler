def sieve_totient(N):
    phi = [i for i in range(N+1)]
    phi[0] = 0
    phi[1] = 0
    is_prime = [True]*(N+1)

    for i in range(2, N+1):
        if is_prime[i]:
            phi[i] = i-1
            for j in range(2*i, N+1, i):
                is_prime[j] = False
                phi[j] = (phi[j]*(i-1)) // i

    return phi

def solve(d):
    phi = sieve_totient(d)
    print('%d = %d' % (d, sum(phi)))

if __name__ == '__main__':
    solve(8)
    solve(10**6)
