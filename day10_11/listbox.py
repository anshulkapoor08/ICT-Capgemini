from tkinter import *
top = Tk()
listbox = Listbox(top, height=10,
                 width=15,
                 bg="grey",
                 activestyle='dotbox',
                 font="Helvetica",
                 fg="yellow")
def change_bg_color(event):
    selected_color = listbox.get(listbox.curselection())
    top.configure(bg=selected_color)
top.geometry("300x250")
label = Label(top, text="Choose Color")
listbox.insert(1, "Orange")
listbox.insert(2, "Blue")
listbox.insert(3, "Red")
listbox.insert(4, "Yellow")
listbox.insert(5, "Purple")
listbox.bind("<<ListboxSelect>>", change_bg_color)
label.pack()
listbox.pack()
top.mainloop()