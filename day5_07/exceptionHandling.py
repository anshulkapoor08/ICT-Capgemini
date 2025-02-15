#Exception handling program
try:
    x=int(input("Enter a number: "))
    y=int(input("Enter another number: "))
    result=x/(y-3)
    print("Result: %.2f"%result)
except ValueError:
    print("value error occured")
except ZeroDivisionError:
    print("Division by zero is not allowed")
except IOError:
    print("IO error occured")
except MemoryError: 
    print("Memory error occured")        
except:
    print('sorry exception occured')       
finally:
    print("everything is done")    