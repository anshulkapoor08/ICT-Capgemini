# Creating Our Own Exception

class MyException(Exception):   # Exception is a predefined class in Python
    pass       # No Coding is required
class MyException1(Exception):
    pass

while True:
    try:
        empname=input("Enter Employee Name ").upper().strip()
            
        if( len(empname)==0):
            raise MyException1
        else:
            break
    except MyException1:   # Special Excepion Handler
        print("Name Can Not Be Blank Or It Should Not Contain any Digits")
        continue
    except:       # Default Exception Handler
        print("Some Other Exception")
        
while True:
    try :
        
        age=int(input("Enter Age "))
        if( age < 21 or age >=60):
            raise MyException # To raise the exception forcefully
            
        print("Employee Name = "+empname)
        print("Age of Employee =%d " %(age))
        break
    except ValueError:
        print("Improper Nos Entered...")
        continue
    except IOError:
        print("KeyBoard Failure Or Any Hardware Failure.....")
        continue
    except MyException:
        print("Age Can Not Be Less than 21 or >= 60")
        continue
    except :  # Default Exception Handler
        print("Sorry Exception Occured...")
        continue
    finally:
        print("Thanks")
print("Program Ended")