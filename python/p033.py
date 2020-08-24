if __name__ == '__main__':
    for a in range(11, 100):
        for b in range(a+1, 100):
            if (a%10 == 0 and b%10==0) or a==b:
                pass
            elif a%10 == b//10 and b%10!=0 and a/b == (a//10)/(b%10):
                print('%d / %d' % (a, b))
            elif a//10 == b%10 and a/b == (a%10)/(b//10):
                print('%d / %d' % (a, b))
            elif a//10 == b//10 and b%10!=0 and a/b == (a%10)/(b%10):
                print('%d / %d' % (a, b))
            elif a%10 == b%10 and a/b == (a//10)/(b//10):
                print('%d / %d' % (a, b))
