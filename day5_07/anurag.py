# Class & Objects
# if i want to define any other fxn member inside then it takes at least one argument.
import os
class Book:
    
    def __init__(myobj,pname="Publisher"):
        # myobj.BookName=""
        # myobj.AuthorName=""
        # myobj.price=0
        myobj.publisher=pname
        
    def EnterBookDetail(myobj):
        myobj.BookName=input("Enter Book Name ").strip().title()
        myobj.AuthorName=input("Enter Author Name ").strip().title()
        myobj.price=int(input("Enter Price "))
       # myobj.publisher=input("Enter Publisher Name ").strip().title()
        
    def grreeting(m1) :
        print("Hello");   

    def ShowBookDetail(myobj):
        heading="List of Books"
        print(heading)
        print("Book Name =",myobj.BookName)
        print("Author Name =", myobj.AuthorName)
        print("Price =%.2f" %myobj.price)
        print("Publisher =",myobj.publisher)
    # w for write mode
    # a for append mode and it is used to add the content at the end of the file.  
    #content stored in the file is in the form of byte.   
    def filestore(myobj):
        try:
            fv=open("C:\\Users\\Anshul chaurasiya\\Desktop\\ICT python\\kp.txt","a")   
            data=myobj.BookName+","+myobj.AuthorName+","+str(myobj.price)+","+myobj.publisher+"\n"
            fv.write(data)
            #fv.close()
            print("Data is stored in the file")
            
        except PermissionError:
            print("File is not accessible") 
            
        except Exception as p1:
            print("Error Occured",p1)      
            
        finally:
            fv.close()
            print("Thanks")    
            
     # Now Add another Functionality say ReadFile() so that we can see the File Content and Count No of Records, also the Size of the File
    def readfile(myboj):
        try:
            fv=open("C:\\Users\\Anshul chaurasiya\\Desktop\\ICT python\\kp.txt","r")
            data=fv.read()
            print(type(data))
            print(data)
            lines=data.split("\n")
            print("No of Records=",len(lines)-1)
            size=os.path.getsize("C:\\Users\\Anshul chaurasiya\\Desktop\\ICT python\\kp.txt")
            print("Size of the file=",size) 
            fv.close()
            print("Data is read from the file")
        except FileNotFoundError:
            print("File is not available")
        
        except PermissionError:
            print("File is not accessible")
            
        finally:
            fv.close()
            print("Thanks")       
                    

    
book1=Book()  # Creating an object book1
# book1.grreeting()
# book1.EnterBookDetail() # Book.EnterDetail(book1)
# book1.ShowBookDetail()  # Book.ShowDetail(book1)

# book1.filestore()


# book2=Book("Oxford")  # Creating an object book2
# book2.EnterBookDetail() # Book.EnterDetail(book2)
# book2.ShowBookDetail()  # Book.ShowDetail(book2)
# book2.filestore()

#book1.readfile()
# book2.readfile()

class Sellbook(Book):
    def Enterdetail(newobj):
        newobj.customer=input("Enter Customer Name ").strip().title()
        newobj.quantity=int(input("Enter Quantity "))
        
    def ShowDetail(newobj):
        print("Customer Name="+newobj.customer)
        print("Quantity="+ str(newobj.quantity))
        
        
customer1=Sellbook()
customer1.EnterBookDetail()
customer1.Enterdetail()
customer1.ShowBookDetail()
customer1.ShowDetail()  