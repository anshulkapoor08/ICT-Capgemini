while True: 
    try:
        x=int(input("Enter a number: "))
        y=int(input("Enter another number: "))
        result=x/(y-3)
        print("Result: %.2f"%result)
        break
    except ValueError:
        print("value error occured")
        continue
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        continue
    except IOError:
        print("IO error occured")
        break
    except MemoryError: 
        print("Memory error occured") 
        break       
    except:
        print('sorry exception occured')       
        
    finally:
        print("everything is done")
       
  