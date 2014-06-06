def is_palindrome(n):
    ns = str(n)
    if ns == ns[::-1]:
        return True
    else:
        return False

def reverse(n):
    ns = str(n)
    return int(ns[::-1])

if __name__ == '__main__':
    cnt = 0
    for n in range(1, 10001):
        t = 0
        while True:
            n = n + reverse(n)
            t += 1
            if is_palindrome(n):
                break
            if t >= 50:
                cnt += 1
                break
    print(cnt)

