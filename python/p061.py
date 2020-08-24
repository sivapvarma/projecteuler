from itertools import permutations

def polygonal_generator(s):
    """
        Source: Wikipedia
    """
    def f(n):
        return ((s-2)*n*(n-1))//2 + n
    return f

def poly_fun():
    d = {}
    for k in range(3, 9):
        d[k] = list(filter(lambda n: n < 10000 and n>= 1000, map(polygonal_generator(k), range(1000))))
    return d

def same_end_start(a, b):
	a, b = str(a), str(b)
	if a[-2:] == b[:2]:
		return True
	else:
		return False
    

if __name__ == "__main__":
    poly_nums = poly_fun()
    k1 = 3
    for v1 in poly_nums[k1]:
        for k2, k3, k4, k5, k6 in permutations(range(4, 9)):
            for v2 in poly_nums[k2]:
                if same_end_start(v1, v2):
                    for v3 in poly_nums[k3]:
                    	if same_end_start(v2, v3):
                    		for v4 in poly_nums[k4]:
                    			if same_end_start(v3, v4):
                    				for v5 in poly_nums[k5]:
                    					if same_end_start(v4, v5):
                    						for v6 in poly_nums[k6]:
                    							if same_end_start(v5, v6) and same_end_start(v6, v1):
                    								print(k1, k2, k3, k4, k5, k6)
                    								l = [v1, v2, v3, v4, v5, v6]
                    								print(v1, v2, v3, v4, v5, v6)
                    								print(sum(l))
                    								exit(1) # return can be used here if creating a solve()
            
    
                    
