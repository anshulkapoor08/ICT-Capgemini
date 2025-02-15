#explore how drop down list can be created
from tkinter import *
from tkinter import ttk
def show_selected(event):
    selected = combo.get()
    label.config(text="You selected: " + selected)
    root.configure(bg=selected)
root = Tk()
root.geometry("500x700")
root.title("Selected Item")
label = Label(root, text="selected")
label.pack()
combo = ttk.Combobox(root)
combo['values'] = ('red', 'green', 'blue')
combo.bind("<<ComboboxSelected>>",show_selected)

combo.pack()
root.mainloop()