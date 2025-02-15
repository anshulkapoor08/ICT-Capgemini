import tkinter as tk
from tkinter import ttk

def addition(ev):
    firstno = int(entry1.get())
    secondno = int(entry2.get())
    result = firstno+ secondno
    entry3.insert(0,str(result))

def subtraction(ev):
    firstno = int(entry1.get())
    secondno = int(entry2.get())
    result = firstno-secondno
    entry3.insert(0,str(result))

def multiply(ev):
    firstno = int(entry1.get())
    secondno = int(entry2.get())
    result = firstno*secondno
    entry3.insert(0,str(result))

def divide(ev):
    firstno = int(entry1.get())
    secondno = int(entry2.get())
    result = firstno/secondno
    entry3.insert(0,str(result))
 
root = tk.Tk() #Creating window
root.title(" My first gui")
root.geometry("350x400")  #root.geometry("widthxheight")
root.configure(bg = "light green")

label1 = ttk.Label(root,text="First Number") # Here Label is a  
#label1.pack() # to make the component visible
entry1=ttk.Entry(root)
#entry1.pack()
label2= ttk.Label(root,text="Second Number")
#label2.pack()
entry2 = ttk.Entry(root)
label3= ttk.Label(root,text=" Result")
entry3 = ttk.Entry(root)


btn1 = ttk.Button(root,text = "Add")
btn1.bind("<Button>",addition) #to apply click event
#entry2.pack()
#btn1.pack()
btn2 = ttk.Button(root,text = "Subtract")
btn2.bind("<Button>",subtraction)
#btn2.pack()
btn3 = ttk.Button(root,text = "Multiply")
btn3.bind("<Button>",multiply)
#btn3.pack()
btn4= ttk.Button(root,text = "Divide")
btn4.bind("<Button>",divide)
#btn4.pack()


#hme layout change krna pdega because , sb ek k upr ek aa rhe , acha nhi lg rha h
label1.grid(row=0,column=0,padx = 5,pady = 10)
entry1.grid(row=0,column=1,padx = 5,pady = 10)
label2.grid(row=1,column=0,padx = 5,pady = 10)
entry2.grid(row=1,column=1,padx = 5,pady = 10)
label3.grid(row=2,column=0,padx = 5,pady = 10)
entry3.grid(row=2,column=1,padx = 10,pady = 10)

btn1.grid(row=3,column=0,padx = 5,pady = 20)
btn2.grid(row=3,column=1,padx = 5,pady = 20)
btn3.grid(row=4,column=0,padx = 10,pady = 20)
btn4.grid(row=4,column=1,padx = 10,pady = 20)
root.mainloop()  #Now events can be captured