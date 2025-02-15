# An iterator is an object that contains a countable number of values.
#They implement the iterator protocol, which consist of the methods __iter__() and __next__()
# Iterator are used to iterate over containers like list, tuples, dict, and set etc.

# city = ("Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore") # tuple
city = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]  # list
y = len(city)
city = iter(city)

'''
print(type(city))
next(city)
for x in range(0, y): # last limit is not included
    print(next(city))
print(next(city))
print(next(city))
print(next(city))  '''  

# printing the elements more than the length of the list
print(y)
print(next(city)) #1
print(next(city)) #2
print(next(city)) #3
print(next(city)) #4
print(next(city)) #5
print(next(city)) #6


# Create an iterator
'''
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

The __iter__() method acts similar as _init_(), it can be used to initialize but must always return the iterator object itself.

'''