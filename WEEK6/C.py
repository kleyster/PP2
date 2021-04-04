def find_mull(arr):
	product = 1

	for i in arr:
		product*=i

	print(product)


arr = [8,2,3,-1,7]

find_mull(arr)