# TKinter is used to create GUI based application.
import tkinter as tk
from tkinter import ttk

def addition(ev):
    firstno = int(entry1.get()) # to get the value from the entry box
    secondno = int(entry2.get())
    result = firstno + secondno
    entry3.insert(0,str(result))# to display the result in the entry box

def substraction(ev):
    firstno = int(entry1.get()) # to get the value from the entry box
    secondno = int(entry2.get())
    result = firstno-secondno
    entry3.insert(0,str(result))

def division(ev):
    firstno = int(entry1.get()) # to get the value from the entry box
    secondno = int(entry2.get())
    result = firstno/secondno
    entry3.insert(0,str(result))

def multiplication(ev):
    firstno = int(entry1.get()) # to get the value from the entry box
    secondno = int(entry2.get())
    result = firstno*secondno
    entry3.insert(0,str(result))            

root = tk.Tk() # creating the window 
root.title("My First GUI") # title of the window
root.geometry("350x400")
root.configure(bg="lightblue")

label1 =ttk.Label(root, text='first no')
entry1=ttk.Entry(root) # entry box to take input

label2 =ttk.Label(root, text='second no')
entry2=ttk.Entry(root)

label3 =ttk.Label(root, text='Result')
entry3=ttk.Entry(root)

btn1=ttk.Button(root,text="Add") # button to add two numbers
btn1.bind("<Button>",addition) # binding the button with the function

btn2=ttk.Button(root,text="substracts") # button to add two numbers
btn2.bind("<Button>",substraction) # binding the button with the function

btn3=ttk.Button(root,text="multiplication") # button to add two numbers
btn3.bind("<Button>",multiplication) # binding the button with the function

btn4=ttk.Button(root,text="divison") # button to add two numbers
btn4.bind("<Button>",division) # binding the button with the function




label1.grid(row=0, column=0, padx=5, pady=10)
entry1.grid(row=0, column=1, padx=5, pady=10)
label2.grid(row=1, column=0, padx=5, pady=10)
entry2.grid(row=1, column=1, padx=5, pady=10)
label3.grid(row=2, column=0, padx=5, pady=10)  
entry3.grid(row=2, column=1, padx=5, pady=10)


btn1.grid(row=3,column=0,padx=5,pady=20)
btn2.grid(row=3,column=1,padx=5,pady=20)
btn3.grid(row=4,column=0,padx=10,pady=10)
btn4.grid(row=4,column=1,padx=10,pady=10)

root.mainloop()   # to keep the window open(now events can be captured)