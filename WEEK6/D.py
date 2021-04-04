def reverse_string(st):

	reversed = ''
	i = len(st)

	while i>0:
		reversed+=st[i-1]
		i-=1

	print(reversed)

st = '1234abcd'

reverse_string(st)