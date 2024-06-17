#統計學系 116級 H24124068 陳祥德
thief = 1
s=0
while thief <= 4:
	if thief != 1:
		s=s+1
	if thief == 3:
		s=s+1
	if thief == 4:
		s=s+1
	if bool(thief == 4)==True:
		s=s+1
	if s==3:	
		print('The thief is', thief)
	thief = thief + 1 

#1 said he is not the thief.
#2 said 3 is the thief.
#3 said 4 is the thief.
#4 said 3 is a liar.