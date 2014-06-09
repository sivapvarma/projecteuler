from itertools import count


def main():
    seen = set()
    cnt = 0
    for b in range(1, 10):
        for e in count(1):
            n = b**e
            if len(str(n)) == e:
                seen.add(n)
                cnt += 1
            else:
                break
    print('cnt = %d' % cnt)
    print('Unique: %d' % len(seen))




if __name__ == '__main__':
    main()
