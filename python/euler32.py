import time
import itertools
timer = time.time

def is_pandigital(md, mr, prod):
    cnt = [0]*10
    for d in str(md):
        cnt[int(d)] += 1
    for d in str(mr):
        cnt[int(d)] += 1
    for d in str(prod):
        cnt[int(d)] += 1
    flag = True
    if cnt[0] != 0:
        flag = False
    else:
        for i in range(1, 10):
            if cnt[i] != 1:
                flag = False
                break
    return flag

# brute force
def solve_bf():
    pand_prod = [0]*100000000
    for a in range(1, 10000):
        for b in range(a, 10000):
            if is_pandigital(a, b, a*b):
                pand_prod[a*b] = 1
                print('%d x %d = %d' % (a, b, a*b))
    res = 0
    for i in range(10**6):
        if pand_prod[i]:
            res += i
    return res

# optimized
def solve():
    """
    to numbers with n1 and n2 digits
    min no of digits in prod: n1 + n2 - 1
    max no of digits in prod: n1 + n2

    Counting a*b = prod and b*a=prod as (a, b, a*b) where a < b
    The product cant have 9, 8, 7, 6, 5 because the left cant have a prod
    with that many digits
    product cant have 3, 2, 1 digits because the left side will have a prod
    with min more no of digits
    so prod can only have 4 digits
    left side either (1, 4) or (2, 3)
    """
    pand_prod = set()
    for a in range(1, 100):
        for b in range(100, 10000):
            if pandigital(a, b, a*b):
                pand_prod.add(a*b)
    return sum(pand_prod)

def pandigital(a, b, ab):
    tmp = ''.join(sorted(str(a)+str(b)+str(ab)))
    if tmp == '123456789':
        return True
    else:
        return False

def solve_permute():
    perm = ['1','2','3','4','5','6','7','8','9']
    all_perms  = itertools.permutations(perm)
    products = set()
    for permutation in all_perms:
        permutation = ''.join(permutation) #turn list of digits into  a string
        product = int(permutation[:2]) * int(permutation[2:5])
        product2 = int(permutation[0]) * int(permutation[1:5])
        if product== int(permutation[5:]):
            products.add(product)
        if product2== int(permutation[5:]):
            products.add(product2)
    return sum(products)

if __name__ == '__main__':
    tStart = timer()
    print(solve())
    tEnd = timer()
    print('Time taken: %f seconds.' % (tEnd-tStart))
    tStart = timer()
    print(solve_permute())
    tEnd = timer()
    print('Time taken by permute: %f seconds.' % (tEnd-tStart))
    # currently most optimized solution takes 1 sec
    # can be optimized even more
