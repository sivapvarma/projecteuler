from math import sqrt
if __name__ == '__main__':
    with open('./data/words42.txt') as f:
        words = f.read().strip('\n').split(',')
    print('# of words = %d' % len(words))
    words = [w.strip('"') for w in words]
    cnt = 0
    for w in words:
        tmp = 0
        for c in w:
            tmp += ord(c) - ord('A') + 1
        tmp = 8*tmp+1 # for a triangular no 8*x+1 is perfect square
        if tmp == int(sqrt(tmp))**2:
            cnt += 1
    print(cnt)
