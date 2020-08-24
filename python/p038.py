def is_pandigital(s):
    if ''.join(sorted(s)) == '123456789':
        return True
    else:
        return False

def no_of_digits(n):
    return len(str(n))

if __name__ == '__main__':
    res = 0
    for n in range(1, 10**6):
        s = ''
        i = 1
        while no_of_digits(s) < 9:
            s += str(n*i)
            i += 1
        if is_pandigital(s):
            if res < int(s):
                res = int(s)
    print(res)


