def count_upper(st):
	upper = 0
	lower = 0
	for i in st:
		if i.isalpha():
			if i.isupper():
				upper += 1
			else:
				lower += 1

	print("No. of Upper case characters : "+str(upper))
	print("No. of Lower case Characters : "+str(lower))

st = "The quick Brow Fox"

count_upper(st)