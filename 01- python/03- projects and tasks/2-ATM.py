# dict for Balances
balance = {
    "Adel": 50000, 
    "Ahmed": 25000,
    "Aly": 13000,
    "mona": 7500
}

# List for PINs
pins = [1111, 2222, 3333, 4444]

# Logic Function
def LOGIC(op,name):
    while True:
        if op == 1:
            print("your balance is ", balance[name])
            break
        elif op == 2:
            m_take = int(input("enter the value:"))
            if m_take > balance[name]:
                print("you do not have enough balance")
            else:
                balance[name] -= m_take
                print("please wait while your transaction is processing, your new balance is", balance[name])
            break
        elif op == 3:
            p_take = int(input("enter the value:"))
            balance[name] += p_take
            print("operation done successfully, your new balance is ", balance[name])
            break
        elif op == 4:
            break
        else:
            print("Invalid operation")
    print("thanks\n************")
	
# Main Program
while True:
    scan_pin = int(input("please enter the PIN:"))
    
    if scan_pin in pins:
        print("1.check balance")
        print("2.take money")
        print("3.put money")
        print("4.exit")
        
        operation = int(input("please select the operation:"))
        
        if scan_pin == 1111:
            LOGIC(operation,"Adel")
            
        elif scan_pin == 2222:
            LOGIC(operation,"Ahmed")
            
        elif scan_pin == 3333:
            LOGIC(operation,"Aly")

        elif scan_pin == 4444:
            LOGIC(operation,"mona")
    else:
        print("Invalid PIN, try again")
		
		
		
		
		
		
'''
********************************without using function LOGIC***************************************
#***************dict for Balances***********
balance = {
    "Adel": 50000, 
    "Ahmed": 25000,
    "Aly": 13000,
    "mona": 7500
}

#***************List for PINs***********
pins = [1111, 2222, 3333, 4444]

while True:
    scan_pin = int(input("please enter the PIN:"))
    
    if scan_pin in pins:
        print("1.check balance")
        print("2.take money")
        print("3.put money")
        print("4.exit")
        
        operation = int(input("please select the operation:"))
        
        if scan_pin == 1111:
            while True:
                if operation == 1:
                    print("your balance is ", balance["Adel"])
                    break
                elif operation == 2:
                    m_take = int(input("enter the value:"))
                    if m_take > balance["Adel"]:
                        print("you do not have enough balance")
                    else:
                        balance["Adel"] -= m_take
                        print("please wait while your transaction is processing, your new balance is", balance["Adel"])
                    break
                elif operation == 3:
                    p_take = int(input("enter the value:"))
                    balance["Adel"] += p_take
                    print("operation done successfully, your new balance is ", balance["Adel"])
                    break
                elif operation == 4:
                    break
                else:
                    print("Invalid operation")
            print("thanks\n************")
            
        elif scan_pin == 2222:
            while True:
                if operation == 1:
                    print("your balance is ", balance["Ahmed"])
                    break
                elif operation == 2:
                    m_take = int(input("enter the value:"))
                    if m_take > balance["Ahmed"]:
                        print("you do not have enough balance")
                    else:
                        balance["Ahmed"] -= m_take
                        print("please wait while your transaction is processing, your new balance is", balance["Ahmed"])
                    break
                elif operation == 3:
                    p_take = int(input("enter the value:"))
                    balance["Ahmed"] += p_take
                    print("operation done successfully, your new balance is ", balance["Ahmed"])
                    break
                elif operation == 4:
                    break
                else:
                    print("Invalid operation")
            print("thanks\n************")
            
        elif scan_pin == 3333:
            while True:
                if operation == 1:
                    print("your balance is ", balance["Aly"])
                    break
                elif operation == 2:
                    m_take = int(input("enter the value:"))
                    if m_take > balance["Aly"]:
                        print("you do not have enough balance")
                    else:
                        balance["Aly"] -= m_take
                        print("please wait while your transaction is processing, your new balance is", balance["Aly"])
                    break
                elif operation == 3:
                    p_take = int(input("enter the value:"))
                    balance["Aly"] += p_take
                    print("operation done successfully, your new balance is ", balance["Aly"])
                    break
                elif operation == 4:
                    break
                else:
                    print("Invalid operation")
            print("thanks\n************")
            
        elif scan_pin == 4444:
            while True:
                if operation == 1:
                    print("your balance is ", balance["mona"])
                    break
                elif operation == 2:
                    m_take = int(input("enter the value:"))
                    if m_take > balance["mona"]:
                        print("you do not have enough balance")
                    else:
                        balance["mona"] -= m_take
                        print("please wait while your transaction is processing, your new balance is", balance["mona"])
                    break
                elif operation == 3:
                    p_take = int(input("enter the value:"))
                    balance["mona"] += p_take
                    print("operation done successfully, your new balance is ", balance["mona"])
                    break
                elif operation == 4:
                    break
                else:
                    print("Invalid operation")
            print("thanks\n************")
    else:
        print("Invalid PIN, try again")
'''