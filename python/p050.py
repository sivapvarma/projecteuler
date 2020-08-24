from math import sqrt
import time

def primes_till(n):
    p = [2, 3, 5, 7, 11]
    for i in range(13, n):
        prime = True
        for num in p:
            if num > sqrt(i):
                break
            if i%num == 0:
                prime = False
                break
        if prime:
            p.append(i)
    return p

def sieve_eratosthenes(n):
    is_prime = [True]*n
    for i in range(2, n):
        if is_prime[i]:
            for j in range(2*i, n, i):
                is_prime[j] = False
    primes = [p for p in range(2, n) if is_prime[p]]
    return primes

if __name__ == '__main__':
    tStart = time.time()
    # l = primes_till(1000000)
    l = sieve_eratosthenes(1000000)
    no_of_primes = len(l)
    print(len(l))
    # print(l)
    res = 953
    # find the maximum length sequence
    tmp_sum = 0
    con = 0
    for p in l:
        tmp_sum += p
        con += 1
        if tmp_sum > 1000000:
            break
    print('Maximum no of consecutive primes %d' % con)
    found = False
    while con > 21:
        for s in range(no_of_primes - con + 1):
            tmp = sum(l[s:s+con])
            if tmp >= 1000000:
                break
            if sum(l[s:s+con]) in l:
                found = True
                res = sum(l[s:s+con])
                print(res, con, s)
                break
        if found:
            break
        con = con - 1
    tEnd = time.time()
    print('time taken %f seconds' % (tEnd - tStart))

