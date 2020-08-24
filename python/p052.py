def digits(n):
    tmp = n
    res = set()
    while tmp > 0:
        res.add(tmp%10)
        tmp = tmp//10
    return res


if __name__ == '__main__':
    i = 1000
    print(digits(9876543210))
    while True:
        flag = False
        d = digits(i)
        mul = 2
        while digits(mul*i)==d:
            if mul == 6:
                flag = True
                break
            mul += 1
        if flag:
            print(i)
            break
        i += 1



