class Book:
    def __init__(myobj, pname = "kapoor and sons"): #constructor
        myobj.publisher= pname
    def EnterBookDetail(myobj):
        myobj.BookName=input("Enter Book Name ").strip().title()
        myobj.AuthorName=input("Enter Author Name ").strip().title()
        myobj.price=int(input("Enter Price "))
        #myobj.publisher=input("Enter Publisher Name ").strip().title()
        
    def showmeyouboob(m1):
        print(" nhi dikhayenge ")

    def ShowBookDetail(myobj):
        heading="List of Books"
        print(heading)
        print("Book Name =",myobj.BookName)
        print("Author Name =", myobj.AuthorName)
        print("Price =%.2f" %myobj.price)
        print("Publisher =",myobj.publisher)
    
book1=Book()  # Creating an object book1
book1.EnterBookDetail() # Book.EnterDetail(book1)
book1.ShowBookDetail()  # Book.ShowDetail(book1) '''
book1.showmeyouboob() # Book.showmeyouboob(book1)kp

book2 = Book("KPS")
book2.EnterBookDetail()
book2.ShowBookDetail()

del book1