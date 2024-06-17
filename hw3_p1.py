#H24124068 陳祥德
n=int(input("input the total number of students(n>0):"))
S=[]
i=1
j=0
p=1
while i<=n:
	S.append(i)
	i += 1

while n>2:

	j=0
	if n%3==1:
		while n-2-3*j>=0:
			S.remove(S[n-2-3*j])	
			j+=1
		S.insert(0,S[n-n//3-1])
		S.pop()
	
	elif n%3==2:
		while n-3-3*j>=0:
			S.remove(S[n-3-3*j])	
			j+=1
		S.insert(0,S[n-n//3-1])
		S.insert(0,S[n-n//3-1])	
		S.pop()
		S.pop()

	n=n-n//3
if n==2:
	print(S[1])
elif n==4:
	print(S[3])
if n==1:
	print(1)
print(S)	