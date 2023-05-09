print("press 1 to function [rindex()] info")
print("press 2 to function [rjust() ] info")
print("press 0 to exit ")


while True:
	selection=int(input("->"))
#*******************************************************************************************[rindex()]********************
	if selection==1:
		print("Searches the string for a specified value and returns the last position of where it was found")
		print('''
			txt = "Mi casa, su casa."

			x = txt.rindex("casa")

			print(x)	''')
		
		txt = "Mi casa, su casa."
		x = txt.rindex("casa")
		print(x)
		print("*************************")
#*******************************************************************************************[rjust() ]********************
	if selection==2:
		print("(EX1)\nReturns a right justified version of the string")
		print('''
			txt = "banana"

			x = txt.rjust(20)

			print(x, "is my favorite fruit.")	''')
		txt = "banana"
		x = txt.rjust(20)
		print(x, "is my favorite fruit.")
		
		print("(EX2)")
		print('''
			txt = "banana"

			x = txt.rjust(20, "O")

			print(x)	''')
		txt = "banana"
		x = txt.rjust(20, "O")
		print(x)
		print("*************************")
		
	if selection==0:
		break

