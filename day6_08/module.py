from tkinter import *
window = Tk()

def mouseClick(event):
    print("Mouse clicked at", event.x, event.y)
def mouseEnter(event):
    print("Mouse entered at", event.x, event.y)

label1 = Label(window, text="Choose your option")
label1.place(x=100, y=100)
label1.pack()

button1 = Button(window, text="ok", bg="red", fg="white")
button2 = Button(window, text="cancel", bg="blue", fg="white")

button1.place(x=120, y=150)    
button2.place(x=200, y=150)

button1.pack()
button2.pack()

button1.bind("<Button>", mouseClick)
button2.bind("<Button>", mouseEnter)

window.mainloop()
    