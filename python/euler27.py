from euler import sieve_eratosthenes
import time
timer = time.time

if __name__ == '__main__':
    tStart = timer()
    # b has to be prime as n=0 should be prime
    b_list = sieve_eratosthenes(1000)
    # generate all primes below 10**5 for checking for primality
    primes = sieve_eratosthenes(10**5)
    primes = set(primes)
    res_cnt = 0
    res = 0
    res_a, res_b = 0, 0
    # a should be odd as 1**2 + 1*a + b should be prime/odd
    for a in range(-999, 1000, 2):
        for b in b_list:
            n = 0
            while True:
                tmp = n**2 + n*a + b
                if tmp in primes:
                    pass
                else:
                    break
                n += 1
            if res_cnt < n+1:
                res = a*b
                res_a, res_b = a, b
                res_cnt = n+1
    print('Product %d*%d = %d, Number of primes: %d' % (res_a, res_b, res, res_cnt))
    tEnd = timer()
    print('Time taken: %f seconds' % (tEnd - tStart))
