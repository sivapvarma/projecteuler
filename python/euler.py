def sieve_eratosthenes(n):
    """Returns a list of prime numbers upto n
    uses sieve of eratosthenes
    """
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    primes = [p for p, is_p in enumerate(is_prime) if is_p]
    return primes
