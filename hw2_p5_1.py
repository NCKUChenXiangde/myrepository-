#統計學系 116級 H24124068 陳祥德
N=input("input a nonnegative integer number:")
n=int(N)
a=5**(1/2)
R=(1/a)*(((1+a)/2)**n-((1-a)/2)**n)
r=int(R)
print(r)