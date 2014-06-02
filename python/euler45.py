def generate_triangular(n):
    for i in range(1, n):
        yield i*(i+1)/2

def generate_pentagonal(n):
    for i in range(1, n):
        yield (i*(3*i-1))/2

def generate_hexagonal(n):
    for i in range(1, n):
        yield  i*(2*i-1)

if __name__ == '__main__':
    lim = 100000
    l = list(generate_triangular(3*lim))
    p = list(generate_pentagonal(2*lim))
    h = list(generate_hexagonal(lim))

    # for n in l:
    #     if n in p:
    #         if n in h:
    #             print(n)
    print(set(l) & set(p) & set(h))


