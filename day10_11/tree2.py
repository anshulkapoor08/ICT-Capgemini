from tkinter import ttk
import tkinter as tk

def dropdown_opened():
    selected = combo.get()
    main_window.configure(bg=selected)

main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox(
    values=["orange", "light blue"],
    postcommand=dropdown_opened
)
combo.place(x=50, y=50)
main_window.mainloop()