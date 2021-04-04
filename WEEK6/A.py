def find_max(arr):
	max = 0
	for i in arr:
		if i>max:
			max=i
	print(max)

arr = [6,2,3,4,5]

find_max(arr)