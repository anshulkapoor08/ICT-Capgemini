'''
Decorators are fucntions that modify the behavior of other functions or methods. 

it takes other function as an argument and returns a new function that add some original fucntion without modifying their source code. 

A decorator is symbolized by @decorator_name in python.
'''

def my_decorator(greetings):
    def wrapper():
        print("Something is happening before the function is called.")
        greetings()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
    print("Good Morning!")
say_hello()    