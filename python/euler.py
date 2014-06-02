def sieve_eratosthenes(n):
    is_prime = [True]*n
    for i in range(2, n):
        if is_prime[i]:
            for j in range(2*i, n, i):
                is_prime[j] = False
    primes = [p for p in range(2, n) if is_prime[p]]
    return primes


def gauss_jordan_mine(m, eps=10**(-9)):
    """ Performs Guass Jordan elimination on the augmented matrix m
        converts the 2D array m to row reduced echelon form
        assumes that m is a N x N+1 matrix and a solvable system
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
        for y2 in range(y+1, h):
            c = m[y2][y] / m[y][y]
            for x in range(y, w):
                m[y2][x]  = m[y2][x] - m[y][x]*c
    # Normalize all rows
    for y in range(0, h):
        for x in range(w):
            m[y][x] /= m[y][y]
    return True

def solve_ls(A, b):
    """
    Solves A@x = b
    returns vector x such that A@x = b
    """
    m = [row[:]+[right] for row, right in zip(A, b)]
    return [row[-1] for row in m] if gauss_jordan_mine(m) else None


def gauss_jordan(m, eps = 1.0/(10**10)):
    """Puts given matrix (2D array) into the Reduced Row Echelon Form.
       Returns True if successful, False if 'm' is singular.
       NOTE: make sure all the matrix items support fractions! Int matrix will NOT work!
       Written by Jarno Elonen in April 2005, released into Public Domain"""
    (h, w) = (len(m), len(m[0]))
    for y in range(0,h):
      maxrow = y
      for y2 in range(y+1, h):    # Find max pivot
        if abs(m[y2][y]) > abs(m[maxrow][y]):
          maxrow = y2
      (m[y], m[maxrow]) = (m[maxrow], m[y])
      if abs(m[y][y]) <= eps:     # Singular?
        return False
      for y2 in range(y+1, h):    # Eliminate column y
        c = m[y2][y] / m[y][y]
        for x in range(y, w):
          m[y2][x] -= m[y][x] * c
    for y in range(h-1, 0-1, -1): # Backsubstitute
      c  = m[y][y]
      for y2 in range(0,y):
        for x in range(w-1, y-1, -1):
          m[y2][x] -=  m[y][x] * m[y2][y] / c
      m[y][y] /= c
      for x in range(h, w):       # Normalize row y
        m[y][x] /= c
    return True


def solve(M, b):
    """
    solves M*x = b
    return vector x so that M*x = b
    :param M: a matrix in the form of a list of list
    :param b: a vector in the form of a simple list of scalars
    """
    m2 = [row[:]+[right] for row,right in zip(M,b) ]
    return [row[-1] for row in m2] if gauss_jordan(m2) else None
