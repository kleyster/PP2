def factorial(n):
	fact = 1

	for i in range(n):
		fact*=(i+1)

	print(fact)

factorial(3)