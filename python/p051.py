from euler import sieve_eratosthenes
from itertools import combinations


primes = []
digits = list(map(str, range(10)))
primes_set = set()

def no_of_digits(n):
    return len(str(n))

def prime_digit_replacements(p, n):
    res = 0
    # we don't replace the last digit
    for t in combinations(list(range(no_of_digits(p-1))), n):
        tmp = 0
        for i, d in enumerate(digits):
            lis = [x for x in str(p)]
            for idx in t:
                lis[idx] = d
            temp = int( ''.join(lis) )
            if temp in primes_set:
                tmp += 1
            # early termination already lost more than 2 replacements
            if i+1-tmp > 2:
                break
        if tmp > res:
            res = tmp
    return res


def solve():
    lim = 10**6
    global primes
    primes = sieve_eratosthenes(lim)
    primes = [p for p in primes if len(str(p)) > 4]
    global primes_set
    primes_set = set(primes)
    print('test: %d' % prime_digit_replacements(56003, 2))
    for p in primes:
        d = no_of_digits(p)
        s = str(p)
        if d > 4 and (s.count('0')==3 or s.count('1')==3 or s.count('2')==3):
            print('%d : %d' % (d, p))
            if prime_digit_replacements(p, 3) == 8:
                print('PE51 Ans: %d' % p)
                return None


if __name__ == '__main__':
    solve()
    # for t in combinations(range(4), 3):
    #     print(''.join(map(str, t)))
