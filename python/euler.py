def sieve_eratosthenes(n):
    """Returns a list of prime numbers upto n
    uses sieve of eratosthenes
    """
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    primes = [p for p, is_p in enumerate(is_prime) if is_p]
    return primes


def gauss_jordan(m, eps=10**(-9)):
    """Performs Guass Jordan elimination on the augmented matrix m
       converts the 2D array m to row reduced echelon form
       assumes that m is a N x N+1 matrix and a solvable system
       Returns True if successful, False if 'm' is singular.
    """
    h, w = len(m), len(m[0])

    for y in range(0, h):
        maxrow = y
        for y2 in range(y+1, h):
            if abs(m[y2][y]) > abs(m[y][y]):
                maxrow = y2
        # exchange rows y and maxrow
        m[maxrow], m[y] = m[y], m[maxrow]
        if abs(m[y][y]) <= eps:
            return False
        for y2 in range(0, h):
            c = m[y2][y] / m[y][y]
            if y2 == y:
                continue
            for x in range(y, w):
                m[y2][x]  = m[y2][x] - m[y][x]*c

    # Normalize all rows
    for y in range(0, h):
        c = m[y][y]
        for x in range(w):
            m[y][x] /= c
    return True

def solve_ls(A, b):
    """Solves the Linear System A@x = b
    returns vector x such that A@x = b
    """
    m = [row[:]+[right] for row, right in zip(A, b)]
    return [row[-1] for row in m] if gauss_jordan(m) else None


if __name__ == '__main__':
    A = [[2, -1, 0],
         [-1, 2, -1],
         [0, -1, 2] ]
    print(A)
    b = [1, 0 , 0]
    print(solve_ls(A, b))
    b = [0, 1, 0]
    print(solve_ls(A, b))
    b = [0, 0, 1]
    print(solve_ls(A, b))
