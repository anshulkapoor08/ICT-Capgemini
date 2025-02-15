from tkinter import *

def red():
    root.configure(bg="red")

def blue():
    root.configure(bg="blue")

def green():    
    root.configure(bg="green")

root = Tk()

mainmenu = Menu(root)
root.title("Color window")

m1 = Menu(mainmenu, tearoff=0)#tearoff=0 just not to show the dashed line

m1.add_command(label="Red", command=red) #event associate
m1.add_separator()
m1.add_command(label="Blue", command=blue)
m1.add_separator()#To make a horizonal line within the menu
m1.add_command(label="Green", command=green)   
         
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Color", menu=m1)
root.config(menu=mainmenu)
root.mainloop()