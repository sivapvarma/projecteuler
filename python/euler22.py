if __name__ == '__main__':
	with open('names.txt') as f:
		words = f.read().strip('\n').split(',')
	print(len(words))
	words_list = [w.strip('"') for w in words]
	words_list.sort() # sort list
	print(words_list[-1])
	res = 0
	for i in range(len(words_list)):
		tmp = 0
		for c in words_list[i]:
			tmp += ord(c)-ord('A')+1	
		res += tmp*(i+1)
	print(res)
