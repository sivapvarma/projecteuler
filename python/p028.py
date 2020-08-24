def spiral_cw(size):
    res = 1
    num = 1
    # step size = grid_size - 1
    # grid_size is odd - 3x3, 5x5, 7x7
    #                     2    4    6
    for n in range(2, size, 2):
        for i in range(4):
            num += n
            res += num
    return res

def spiral_cw_formula(size):
    res = 1
    for t  in range(3, size+1, 2):
        """
        top right: t**2
        top left: t**2 -(t-1)
        bottom left: t**2 - 2*(t-1)
        bottom right: t**2 - 3*(t-1)
        """
        res += 4*(t**2) - 6*t + 6
    return res

if __name__ == '__main__':
    print('5x5 spiral: %d' % spiral_cw(5))
    print('5x5 spiral: %d' % spiral_cw_formula(5))
    print('1001x1001 spiral: %d' % spiral_cw(1001))
    print('1001x1001 spiral: %d' % spiral_cw_formula(1001))
