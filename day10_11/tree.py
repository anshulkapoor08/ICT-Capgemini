import tkinter as tk
from tkinter import ttk

def remove_selected():
    selected_item = tree.selection()  # Get selected item
    if selected_item:
        tree.delete(selected_item)

# Function to expand all items
def expand_all():
    for item in tree.get_children():
        tree.item(item, open=True)
        for sub_item in tree.get_children(item):
            tree.item(sub_item, open=True)
            
root=tk.Tk()
root.title("Example of treeview")
root.geometry("600x300")

tree=ttk.Treeview(root)
tree.pack()

master_item= tree.insert(parent="",index="end",id="master_item", text="Master Item")

item1= tree.insert(master_item, index="end", id="item1", text="item 1")
item2= tree.insert(master_item, index="end", id="item2", text="item 2")
item3= tree.insert(master_item, index="end", id="item3", text="item 3")

tree.insert(item1, index="end", id="subitem1_1", text="Subitem 1.1")
tree.insert(item1, index="end", id="subitem1_2", text="Subitem 1.2")

tree.insert(item2, index="end", id="subitem2_1", text="Subitem 2.1")
tree.insert(item2, index="end", id="subitem2_2", text="Subitem 2.2")
tree.insert(item3, index="end", id="subitem3_1", text="Subitem 3.1")
tree.insert(item3, index="end", id="subitem3_2", text="Subitem 3.2")

btn_remove = ttk.Button(root, text="Remove Selected", command=remove_selected)
btn_remove.pack(pady=5)

btn_expand = ttk.Button(root, text="Expand All", command=expand_all)
btn_expand.pack(pady=5)

root.mainloop()