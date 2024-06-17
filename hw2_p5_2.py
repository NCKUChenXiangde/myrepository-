#統計學系 116級 H24124068 陳祥德
t=0
a=0
b=t-a
t=a+b
i=0
f=0
s=input("input the word:")
n=len(s)-1
while s[i+a]==s[n-i-b] and (n+1)//2>=i:
	i=i+1
if (n+1)//2<=i:
	print(s)
while (n+1-t)//2>i:
	a=0
	t=t+1
	while a<=t :
		i=0
		while s[i+a]==s[n-i-b]:
			i=i+1
		if(n+1-t)//2<=i:
			print(s[a+1:n-b-1])
			break
		if (n+1-t)//2>i:
			a=a+1