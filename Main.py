lastNumber = 5
for i in range(lastNumber):
	print(lastNumber,end=" ")	
	a=lastNumber-1
	for n in range(i):
		print(a,end=' ')
		a=a-1
	print("\n")