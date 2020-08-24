from euler import sieve_eratosthenes
import time

primes = []

def factorize(n):
    res = []
    for p in primes:
        if n == 1:
            break
        if n%p == 0:
            e = 0
            while n%p == 0:
                n = n//p
                e += 1
            res.append((p, e))
    return res

# uses sieve to count number of distinct prime factors
def solve_opt():
    max=1000000
    n_factor = [0]*max

    for i in range(2,max): 
        if n_factor[i] == 0 :
            for j in range(2*i,max,i):
                n_factor[j] += 1
    goal = [4]*4
    for i in range(2,max):
         if n_factor[i:i+4] == goal:
            return i

if __name__ == '__main__':
    # start = time.time()
    # primes = sieve_eratosthenes(10**6)
    # n = 2*3*5*7
    # nf = 4
    # ci = 1
    # while ci != 4:
    #     n += 1
    #     # print(n)
    #     if n > 10**6:
    #         print('limit reached!')
    #         break
    #     if len(factorize(n)) == 4:
    #         ci += 1
    #     else:
    #         ci = 0
    # end = time.time()
    # print(n-3)
    # print('Time taken: %f seconds.' % (end-start))
    start = time.time()
    print(solve_opt())
    end = time.time()
    print('Time taken: %f seconds.' % (end-start))


