from fractions import Fraction as F
from fractions import gcd


def main():
    den = 10**4
    l = []
    for d in range(den, 0, -1):
        s, u = (428*d)//999, d//2
        print(d, s, u)
        for n in range(s + 1, u + 1):
            frac = F(n, d)
            l.append(F(n, d))
            # if not frac in l:
            #     l.append(F(n, d))
    print('created!')
    l.sort()
    prev = 0
    for frac in l:
        if frac == F(3, 7):
            break
        prev = frac
    print(prev)


def solve():
    den = 10**6
    l = []
    res = 0
    sentinel = F(3, 7)
    for d in range(2, den+1):
        # for n in range(1, d):
        # s, u = (428*d)//999, d//2
        # s, u = (4283*d)//9994, d//2
        s, u = (42857*d)//100000, d//2
        s, u = (428570*d)//999997, d//2
        print(d, s, u)
        for n in range(s + 1, u + 1):
            if gcd(n, d) == 1:
                # l.append(F(n, d))
                tmp = F(n, d)
                if tmp > res:
                    if tmp < sentinel:
                        res = tmp
                    else:
                        break
    print(res)
    # print('Created!')
    # l.sort()
    # print('sorted!')
    # prev = 0
    # for frac in l:
    #     if frac == F(3, 7):
    #         break
    #     prev = frac
    # print(prev)

def solve_optimized():
    """Shamelessly copied from overview for prob 71
    I just can't believe I couldn't think of this. - 11/June/2014
    """
    num = 3
    den = 7
    best_num = 0
    best_den = 1
    cur_den = 10**140
    min_den = 1
    while cur_den > min_den:
        # for every denominator we need to consider only one numerator
        cur_num = (num*cur_den - 1)//den
        if best_num*cur_den < cur_num*best_den:
            best_num = cur_num
            best_den = cur_den
            delta = num*cur_den - den*cur_num
            min_den = (cur_den // delta) + 1
        cur_den -= 1
    print(best_num, best_den)

if __name__ == '__main__':
    # main()
    # solve()
    solve_optimized()
