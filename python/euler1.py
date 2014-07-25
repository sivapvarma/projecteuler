from __future__ import print_function, division


def solve(lim):
	res = 0
	for n in range(1000):
		if n%3==0 or n%5==0:
			res += n
	return res

if __name__ == '__main__':
	print(solve(1000))