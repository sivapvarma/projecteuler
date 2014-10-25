from euler import sieve_eratosthenes

if __name__ == '__main__':
    limit = 100
    ways = [1] + [0]*limit
    T = 5000
    primes = sieve_eratosthenes(limit)
    for p in primes:
        for i in range(p, limit+1):
            ways[i] += ways[i-p]
    for n, t in enumerate(ways):
        if t > T:
            print("PE77 Ans: %d\n" % n)
            break
