def cross(A, B):
    """Cross product of elements in A and elements in B"""
    return [a+b for a in A for b in B]

digits = '123456789'
rows   = 'ABCDEFGHI'
cols   = digits
squares = cross(rows, digits)
unitslist = ([cross(rows, c) for c in cols] +
             [cross(r, cols) for r in rows] +
             [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

units = {s:[u for u in unitslist if s in u] for s in squares}

#peers = {s:(set(sum(units[s], []))-set([s])) for s in squares}
peers = {s:{sq for u in units[s] for sq in u if sq != s} for s in squares}

def parse_grid(grid):
    """Convert grid to a dict of possible values, {square:digits}, or
    return False if a contradiction is detected."""
    # To start, every square canbe any digit; then assign values from the grid
    values = {s:digits for s in squares}
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False # Fail if we cant assign d to square s
    return values

def grid_values(grid):
    "Convert grid into a dict of {square:char} with '0' or '.' empties."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

## Constraint Propagation

def assign(values, s, d):
    """Eliminate all the other values (except d) from vlaues[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    #display(values)
    #print('Assign', s, d)
    #print('Assign','values['+s+']', values[s])
    other_values = values[s].replace(d, '')
    #print('other_values', other_values)
    #print('Assign','values['+s+']', values[s])
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        #print('Contradiction in Assign')
        return False

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    #print('Eliminate ', s, d)
    if d not in values[s]:
        #print('Already eliminated')
        return values # Already eliminated
    #print('values['+s+']', values[s])
    values[s] = values[s].replace(d, '')
    #print('values['+s+']', values[s])
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers
    if len(values[s]) == 0:
        #print('Contradiction: removed last value')
        return False # Contradiction: removed last value
    elif len(values[s]) == 1:
        #print('len 1')
        d2 = values[s]
        #if s in peers[s]:
        #    print('Here is the issue')
        # if there is only one option for s, eliminate that option
        # if you cant eliminate that from peers there is a problem
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            #print('Contradiction: len 1')
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            #print('Contradiction')
            return False # Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit: assign it there
            if not assign(values, dplaces[0], d):
                #print('Contradiction')
                return False
    #print('Eliminated', s, d)
    return values

# Display grid
def display(values):
    """Display these values as a 2D grid."""
    width = 1 + max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(''.join(values[r+c].center(width)+('|' if c in '36' else ''))
                      for c in cols))
        if r in 'CF':
            print(line)
    print()

# Search

def solve(grid):
    return search(parse_grid(grid))

def search(values):
    "Using depth-first search and propagation, try all possible values"
    if values is False:
        return False # Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values # Solved!
    # Choose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

# code specific to this problem
def parse_file(fname):
    with open(fname) as f:
        for j in range(50):
            gname, g = '', ''
            gname    = f.readline()
            for i in range(9):
                g += f.readline()
            yield gname, g

if __name__ == "__main__":
    ans = 0
    # read puzzle by puzzle and solve them and print them
    for gname, g in parse_file('../data/p096_sudoku.txt'):
        print(gname.strip())
        print(g.strip())
        #display(parse_grid(g))
        #display(solve(g))
        values = solve(g)
        tmp = 0
        for s in ['A1', 'A2', 'A3']:
            tmp = tmp*10 + int(values[s])
        ans += tmp
    print('PE #96 Ans:', ans)
