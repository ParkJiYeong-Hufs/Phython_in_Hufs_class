lastNumber = 5
for i in range(lastNumber):
	print(lastNumber,end=" ")	
	a=lastNumber-1
	for n in range(i):
		print(a,end=' ')
		a=a-1
	#print(' ')를 쓰면 줄 바꾸기가 자동으로 되기 때문에 줄 안바꾸고 이어서 쓰고 싶으면 위에 처럼 end=' '를 사용하기
	print("\n")
