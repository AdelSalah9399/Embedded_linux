import os
import time

'''****************RIGHT arrow***********************************'''
def R_arrow():
 print('''













 
                                                                                                                                         *
                                                                                                                                         **
                                                                                                                                         ****
                                                                                                                                         *****
                                                                                                                                         ******
                                                                                                 ***********************************************
                                                                                                 ************************************************
                                                                                                 ***********************************************
                                                                                                                                         ******
                                                                                                                                         *****
                                                                                                                                         ****
                                                                                                                                         **
                                                                                                                                         *
 ''')

'''****************LEFT arrow***********************************'''
def L_arrow():
 print('''













 
                                                      *
                                                     **
                                                    ***
                                                   ****
                                                  *****
                                                 ***********************************************
                                                ************************************************
                                                 ***********************************************
                                                  *****
                                                   ****
                                                    ***
                                                     **
                                                      *
 ''')

'''****************UP arrow 2***********************************'''
def U_arrow():
 print('''
 
                                                                                                *
                                                                                               ***
                                                                                             ********
                                                                                          **************
                                                                                       ********************
                                                                                     ************************
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
 ''')
'''****************Down arrow 2***********************************'''
def D_arrow():
 print('''
 














																					  
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                               *****
                                                                                      ************************
                                                                                        ********************
                                                                                           **************
                                                                                              ********
                                                                                                ***
                                                                                                 *
 ''')
	

while True:
	dir=int(input("Enter the Direction\nClockwise->1\nCounter Clockwise->2\n"))
	if dir==1:
		while True:
			os.system('cls')
			R_arrow()
			time.sleep(1)
			os.system('cls')
			D_arrow()
			time.sleep(1)
			os.system('cls')
			L_arrow()
			time.sleep(1)
			os.system('cls')
			U_arrow()
			time.sleep(1)
			os.system('cls')
	elif dir==2:
		while True:
			os.system('cls')
			R_arrow()
			time.sleep(1)
			os.system('cls')
			U_arrow()
			time.sleep(1)
			os.system('cls')
			L_arrow()
			time.sleep(1)
			os.system('cls')
			D_arrow()
			time.sleep(1)
			os.system('cls')
	else:
		print("worng entry try again")


