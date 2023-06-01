import os

os.system('cls')
print("						CLCULATOR")

while True:
	select=int(input("Please select the mode:\n1-Standard mode\n2-Programer mode\n"))
	if select == 1:
	 print(">>>>>>>>>>Standard mode<<<<<<<<<<<<<")
	 op1=int(input("enter number 1\n "))
	 operation=input("select the operation\n ")
	 op2=int(input("enter number 2\n "))
	 if operation == '+':
	  print("result = ",op1+op2)
	 elif operation == '-':
	  print("result = ",op1-op2)
	 elif operation == '*':
	  print("result = ",op1*op2)
	 elif operation == '/':
	  print("result = ",op1/op2)
	 elif operation == '%':
	  print("result = ",op1%op2)
	 
	 print("thank you\n*******************************************************")
	 
	if select == 2:
	 print(">>>>>>>>>>programer mode<<<<<<<<<<<<<")
	 op1=int(input("enter number 1\n "))
	 operation=input("select the operation\n ")
	 op2=int(input("enter number 2\n "))
	 if operation == '+':
	  print("result = ",op1+op2)
	 elif operation == '-':
	  print("result = ",op1-op2)
	 elif operation == '*':
	  print("result = ",op1*op2)
	 elif operation == '/':
	  print("result = ",op1/op2)
	 elif operation == '%':
	  print("result = ",op1%op2)
	 elif operation == '>>':
	  print("result = ",op1>>op2)
	 elif operation == '<<':
	  print("result = ",op1<<op2)
	 
	 print("thank you\n*******************************************************")
