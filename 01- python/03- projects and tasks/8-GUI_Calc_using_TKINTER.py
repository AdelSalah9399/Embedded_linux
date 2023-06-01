import tkinter 
from tkinter import *

root = Tk()
root.geometry("570x600+300+10")
root.title("Calculator")
root.resizable(False,False)
root.configure(bg="#17161b")

showed_data = ""

def show(data):
    global showed_data
    showed_data += data
    Lable_res.config(text=showed_data)

def clear():
	global showed_data
	showed_data=""
	Lable_res.config(text=showed_data)

def calc():
	global showed_data
	res=""
	if showed_data !="":
		try:
			res= eval(showed_data)
		except:
			res="error"
			#showed_data=""
	Lable_res.config(text=res)

	


Lable_res=Label(root, width=25 , height=2 , text="" , font=("arial",30))
Lable_res.pack()

Button(root, text="C" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#3697f5" , command=lambda:clear()).place(x=10,y=100)
Button(root, text="/" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("/")).place(x=150,y=100)
Button(root, text="%" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("%")).place(x=290,y=100)
Button(root, text="*" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("*")).place(x=435,y=100)

Button(root, text="7" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("7")).place(x=10,y=200)
Button(root, text="8" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("8")).place(x=150,y=200)
Button(root, text="9" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("9")).place(x=290,y=200)
Button(root, text="+" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("+")).place(x=435,y=200)

Button(root, text="4" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("4")).place(x=10,y=300)
Button(root, text="5" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("5")).place(x=150,y=300)
Button(root, text="6" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("6")).place(x=290,y=300)
Button(root, text="-" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("-")).place(x=435,y=300)

Button(root, text="1" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("1")).place(x=10,y=400)
Button(root, text="2" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("2")).place(x=150,y=400)
Button(root, text="3" , width=5 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("3")).place(x=290,y=400)

Button(root, text="=" , width=5 , height=3 , font=("arial",30) , bd=1 , fg="#fff" , bg="#fe9037" , command=lambda:calc()).place(x=435,y=400)

Button(root, text="." , width=5  , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show (".")).place(x=290,y=500)
Button(root, text="0" , width=11 , height=1 , font=("arial",30) , bd=1 , fg="#fff" , bg="#2a2d63" , command=lambda:show ("0")).place(x=10,y=500)









root.mainloop()