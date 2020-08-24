from euler import timeit
from math import floor, log10


is_prime = 0

def prime_sieve(lim):
    global is_prime
    is_prime = [True]*(lim+1)
    is_prime[0] = is_prime[1] = False
    for n in range(2, lim+1):
        if is_prime[n]:
            for m in range(2*n, lim+1, n):
                is_prime[m] = False


@timeit
def solve():
    prime_sieve(10**8)
    print('sieve done')
    lim = 10000
    for p1 in range(2, lim):
        if is_prime[p1]:
            for p2 in range(p1+1, lim):
                if is_prime[p2] and is_prime_pair(p2, p1):
                    for p3 in range(p2+1, lim):
                        if is_prime[p3] and is_prime_pair(p3, p1) and is_prime_pair(p3, p2):
                            for p4 in range(p3+1, lim):
                                if is_prime[p4] and is_prime_pair(p4, p1) and is_prime_pair(p4, p2) and is_prime_pair(p4, p3):
                                    print(p1, p2, p3, p4)
                                    for p5 in range(p4+1, lim):
                                        if is_prime[p5] and is_prime_pair(p5, p1) and is_prime_pair(p5, p2) and is_prime_pair(p5, p3) and is_prime_pair(p5, p4):
                                            print(p1, p2, p3, p4, p5)
                                            return None


def is_prime_pair(n1, n2):
    return is_prime[int(str(n1)+str(n2))] and is_prime[int(str(n2)+str(n1))]



@timeit
def solve_op():
    lim = 10000
    prime_sieve(lim)
    print('sieve done')
    for p1 in range(3, lim, 2):
        if is_prime[p1]:
            for p2 in range(p1+2, lim, 2):
                if is_prime[p2] and prime_pair(p2, p1):
                    for p3 in range(p2+2, lim, 2):
                        if is_prime[p3] and prime_pair(p3, p1) and prime_pair(p3, p2):
                            for p4 in range(p3+2, lim, 2):
                                if is_prime[p4] and prime_pair(p4, p1) and prime_pair(p4, p2) and prime_pair(p4, p3):
                                    print(p1, p2, p3, p4)
                                    for p5 in range(p4+2, lim, 2):
                                        if is_prime[p5] and prime_pair(p5, p1) and prime_pair(p5, p2) and prime_pair(p5, p3) and prime_pair(p5, p4):
                                            print(p1, p2, p3, p4, p5)
                                            print('PE60 Ans: %d' % sum((p1, p2, p3, p4, p5)))
                                            return None


# def prime_pair(n1, n2):
#     return prime(int(str(n1)+str(n2))) and prime(int(str(n2)+str(n1)))


def prime_pair(n1, n2):
    t1 = n1*(10**floor(log10(n2)+1)) + n2
    t2 = n2*(10**floor(log10(n1)+1)) + n1
    return prime(t1) and prime(t2)


def prime(n):
    lim = round(n**0.5)
    for i in range(2, lim+1):
        if n%i == 0:
            return False
    return True


if __name__ == '__main__':
    # solve()
    solve_op()
