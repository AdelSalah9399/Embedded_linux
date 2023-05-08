# TUPLE using 
# oring with if statment 
# superloop while(1) making

drinks=("cocc-colla","pepsi","merenda")
ships=("laiz","chipsy","tiger")

price_dict={
	"cocc-colla": 8,
	"pepsi": 7,
	"merenda": 8,
	"laiz": 35,
	"chipsy": 10,
	"tiger": 5
}
print("DRINK product:",drinks,"\nSHIPS product:",ships,"\n")
while True:
	price=input("Hello--Enter the product name to get its Price:")
	if price in drinks or price in ships:     #how to use if in new way
		print("the price is ",price_dict[price],"\nhave a good day\n","****************")
	else:
		print("wrong enter -no such product- please try again")
