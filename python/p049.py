from euler import sieve_eratosthenes
from itertools import permutations

def permuted_digits(m, n):
    ms,ns = str(m),str(n)
    ma,na = [0]*10, [0]*10
    for a in ms:
        ma[int(a)] += 1
    for a in ns:
        na[int(a)] += 1
    flag = True
    for i in range(10):
        if na[i] != ma[i]:
            flag = False
    return flag

def tuple2int(tup):
    res = 0
    for i in tup:
        res = res*10
        res = res + int(i)
    return res

if __name__ == '__main__':
    primes = sieve_eratosthenes(9999)
    p = [n for n in primes if len(str(n))==4]
    print('%d four digit primes' % len(p))
    # print(p)
    # for r in range(2, 4500, 2):
    #     for num in p:
    #         if num+r in p:
    #             if num+2*r in p:
    #                 if permuted_digits(num, num+r) and permuted_digits(num, num+2*r):
    #                     print(num, num+r, num+2*r)
    for num in p:
        cnt = 0
        l = [num]
        for tup in permutations(str(num)):
            tmp = tuple2int(tup)
            if (not tmp in l) and tmp in p:
                cnt += 1
                l.append(tmp)
        if cnt==2:
            # if l[1]-l[0]==l[2]-l[1]:
            print(l)
