import time

def sum_of_digits(n):
    r = 0
    for i in str(n):
        r += int(i)
    return r

if __name__ == '__main__':
    # print(sum_of_digits(99))
    m = 0
    lim = 101
    tStart = time.time()
    for b in range(1, lim):
        for a in range(2, lim):
            tmp = sum_of_digits(a**b)
            if tmp > m:
                m = tmp
                # print(a, b, m)
    tEnd = time.time()
    print(m)
    print('Runtime: %f seconds.' % (tEnd-tStart))

