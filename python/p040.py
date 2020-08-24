if __name__ == '__main__':
    s = ''
    l = 10**6
    i = 1
    while len(s)<l:
        s += str(i)
        i += 1
    print(int(s[0])*int(s[9])*int(s[99])*int(s[999])*int(s[9999])*int(s[99999])*int(s[999999]))
