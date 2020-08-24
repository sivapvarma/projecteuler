from itertools import permutations
import time

if __name__ == '__main__':
    start = time.time()
    s = '0123456789'
    cnt = 0
    for p in permutations(list(s)):
        if p[0] != '0':
            if ( int(''.join(p[1:4]))%2==0
                 and int(''.join(p[2:5]))%3==0
                 and int(''.join(p[3:6]))%5==0
                 and int(''.join(p[4:7]))%7==0
                 and int(''.join(p[5:8]))%11==0
                 and int(''.join(p[6:9]))%13==0
                 and int(''.join(p[7:10]))%17==0):
                cnt += int(''.join(p))
    end = time.time()
    print(cnt)
    print('solved in %f seconds' % (end-start))

