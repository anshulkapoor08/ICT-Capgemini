import tabulate

table = [["Sun",10],["Earth",6371, "terrestial"],["Moon",1737,"terrestial"],["Mars",3390,"terrestial"],["Jupiter",69911,"gas giant"],["Saturn",58232,"gas giant"],["Uranus",25362,"ice giant"],["Neptune",24622,"ice giant"]] 
print(tabulate.tabulate(table, headers =["Name", "Radius", "Type"]))