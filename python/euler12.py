from euler import sieve_eratosthenes

if __name__ == '__main__':
    primes = sieve_eratosthenes(1000000)
    div_req = 500
    tri = 0
    i = 1
    while True:
        tri = tri + i
        i = i + 1
        # find number of divisors
        div = 1
        tmp = tri
        for p in primes:
            cnt = 0
            while tmp%p == 0:
                tmp = tmp/p
                cnt += 1
            div = div*(cnt+1)
            if tmp == 1:
                break
        if div > div_req:
            print('First triangle number to have over 500 divisors: %d' % tri)
            break




