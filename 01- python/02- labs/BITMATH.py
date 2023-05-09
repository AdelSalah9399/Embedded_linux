def setbit(reg,bit):
	reg|=(1<<bit)
	return reg
	
def clrbit(reg,bit):
	reg&=(~(1<<bit))
	return reg
	
def bit(reg,bit):
	reg^=(1<<bit)
	return reg

	
def getbit(reg,bit):
	(reg>>bit)&1
	return reg

	
print(setbit(2,0))

for i in range(7,0,-1):
	print(i)