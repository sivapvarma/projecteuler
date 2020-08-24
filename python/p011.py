if __name__ == '__main__':
    grid = []
    with open('11.txt') as f:
        for line in f.readlines():
            arr = line.strip('\n').split(' ')
            arr1 = [int(n) for n in arr]
            grid.append(arr1)
    print(grid)
    res = 0
    direc = ''
    i_max = 0
    j_max = 0
    for i in range(20):
        for j in range(20):
            # right
            if j+3 < 20:
                tmp = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
                if tmp > res:
                    res = tmp
                    direc = 'right'
                    i_max, j_max = i, j
            # down
            if i+3 < 20:
                tmp = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
                if tmp > res:
                    res = tmp
                    direc = 'down'
                    i_max, j_max = i, j
            # principal diagonal
            if i+3 < 20 and j+3 < 20:
                tmp = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
                if tmp > res:
                    res = tmp
                    direc = 'right diagonal'
                    i_max, j_max = i, j
            # other diagonal
            if i+3 < 20 and j-3 >= 0:
                tmp = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
                if tmp > res:
                    res = tmp
                    direc = 'left diagonal'
                    i_max, j_max = i, j
    # final result
    print('Ans: %d\ndirec: %s\ni, j = %d, %d' % (res, direc, i_max, j_max))
