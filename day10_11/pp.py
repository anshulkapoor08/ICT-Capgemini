#findings duplicate items
# Finding Duplicate Entries Only
from collections import Counter

items = ("Mouse", "Headphone", "Keyboard", "Mic", "Mouse Pad", "Mic", "Mouse", "Table", "HeadPhone", "AV Software", "Mouse Pad")

mylist = []
for x in items:
    mylist.append(x.upper())

searchitems = Counter(mylist).items()
myitems = list(searchitems)
print(myitems)

print("Duplicate Items Are")
for x in myitems:
    if x[1] > 1:
        print(x[0])