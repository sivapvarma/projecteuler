from math import log


def main():
    i = 1
    res = 1
    val = 0
    with open('../data/p099_base_exp.txt') as f:
        for line in f:
            b, e = line.rstrip().split(',')
            b, e = int(b), int(e)
            tmp = e*log(b)
            if tmp > val:
                res = i
                val = tmp
            i += 1
    print(res)


if __name__ == '__main__':
    main()
