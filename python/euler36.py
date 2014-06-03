def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    res = 0
    for i in range(1, 10**6):
        if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
            res += i
    print(res)
