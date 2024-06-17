layer=input("Enter the number of layers(2~5):")
length_top=input("Enter the side length of the top layer(2~6):")
layer_growth=input("Enter growth of each layer(1~):")
width_trunk=input("Enter the trunk width(odd,3~9):")
height_trunk=input("Enter the trunk height(4~10):")
L=int(layer)
Lt=int(length_top)
Lg=int(layer_growth)
w=int(width_trunk)
h=int(height_trunk)
j=int((Lt-1)+(L-1)*Lg)


print(" "*(j)+"#")
t=1
n=0
f=0
while t<=L:
	i=0
	while i < Lt-2+n:
		print(" "*(j-i-1)+"#"+"@"*(1+(2*i))+"#")
		i=i+1
	
	print(" "*(j+1-Lt-Lg*f)+"#"*(2*Lt-1+2*Lg*f))
	f=f+1
	t=t+1
	n=n+Lg
Y=j-((w-1)/2)
y=int(Y)
p=1
while p <= h :
	print(" "*(y)+"|"*w)
	p=p+1
