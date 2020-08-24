def main(lim):
	res = 0
	prev, n = 0, 1
	while n <= lim:
		# print(n)
		if n%2 == 0:
			res += n
		prev, n = n, prev+n
	return res


if __name__ == '__main__':
	print(main(4000000))