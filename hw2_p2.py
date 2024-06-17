#統計學系 116級 H24124068 陳祥德
x=int(input("please input a positive integer:")) #d(N) f(Z)
S=[]
y=x
p=y
while x>2:
	if (2**(x-1))%x==1:
		S.append(x)
		x-=1
	else:
		x-=1
S.append(2)
S.reverse()
#將小於輸入值的所有質數列為串列

n=len(S)
U=[]
W=[]
i,j=0,0
while i<n:
	if y%S[i]!=0:
		i+=1
		U.append(0)
	else:
		j=0
		while y%S[i]==0:
			y=y/S[i]
			j+=1
		U.append(j)
		i+=1
		W.append(i-1)
#將輸入值因數分解並把個別次方列為字串
w=len(W)
k=0
V=[]
T=[]
if p!=1:
	g=U[W[k]]
r=0
if w!=0 :
	while k<w:
		g=U[W[k]]
		V=[]
		r=0
		while g!=-1:
			V.append(S[W[k]]**g)
			g=g-1
		k=k+1
		r=sum(V)
		T.append(r)
from functools import reduce
c=p
if p!=1:
	c=reduce((lambda x, y: x * y ),T)
print(c)
"""	
if c/2==p:
	print("Yes")
print(S)
print(U)
print(W)
print(T)
"""








