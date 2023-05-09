import os
import time


#h=7
#flag=1
#flag2=1
'''****************UP arrow***********************************'''
'''
for i in range(1,h+1):
	#print spaces with shifting mechanism
	for j in range(1,h-i+1):
		if flag==1:
			print("						",end="")
		print(" ",end="")
		flag=0
	#print stars with shifting mechanism
	for k in range(1,2*i):
		if flag2==7:
			print("						",end="")
			flag2=0
		print("*",end="")
	#new line and update the flags
	print()
	flag=1
	flag2 += 1
	#draw the vertical line
for i2 in range(10):
	print("						      **")
'''
'''****************DOWN arrow***********************************'''
'''
flag = 1
flag2 = 7
	#draw the vertical line
for i2 in range(10):
	print("						      **")
# Loop through each row of the pyramid in reverse order
for i in range(h, 0, -1):
    # Print out spaces with shifting mechanism
    for j in range(h - i):
        if flag == 1:
            print(" 			                       ", end="")
        print(" ", end="")
        flag = 0

    # Print out stars with shifting mechanism
    for k in range(2 * i - 1):
        if flag2 == 7:
            print(" 			                       ", end="")
            flag2 = 0
        print("*", end="")

    # New line and update the flags
    print()
    flag = 1
    flag2 += 1
'''
'''****************RIGHT arrow***********************************'''