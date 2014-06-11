from itertools import combinations_with_replacement as cwr
from itertools import permutations

if __name__ == '__main__':
    with open('cipher1_59.txt', 'r') as f:
        line = f.readline() # only single line in the file

    numbers = line.rstrip().split(',')
    numbers = [int(n) for n in numbers]
    length = len(numbers)
    print(length)

    charset = [' ', ',', '.']
    st = ord('A')
    en = st + 25
    for i in range(st, en+1):
        charset.append(chr(i))
    st = ord('a')
    en = st + 25
    for i in range(st, en+1):
        charset.append(chr(i))

    print(''.join(charset))


    for tup in cwr(list(range(st, en+1)), 3):
        for t in permutations(tup):
            s = []
            for i, c in enumerate(numbers):
                # print(chr(numbers[i]^t[i%3]), end='')
                s.append(chr(c ^ t[i%3]))
            cnt = 0
            for c in s:
                if not c in charset:
                    cnt += 1
            if cnt < 50:
                print('Key: ' + ''.join(map(chr, t))+' Errors: '+str(cnt))
                print(''.join(s[0:100]))
                res = 0
                for c in s:
                    res += ord(c)
                print('Ans: %d' % res)
                break
