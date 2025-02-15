import sqlite3
db_file = "kapoorDatabase.db" 
try:
    conn = sqlite3.connect(db_file) #Connection object
    cur = conn.cursor() #Creationg the cursor object
    cur.execute("SELECT * FROM ItemMaster")
    
    count = 0
    print('List of items:')
    rows = cur.fetchall() 
    for row in cur:
        print(row)
        count+=1
    print("All Rows Displayed")
    print("Total Records = %d" %(count))
except sqlite3.OperationalError:
    print(" Error please check the table name or database")#In case there is connectivity issues
except :
    print(" Database Connectivity")   
finally:
    if 'conn' in locals(): #Checking if the connection object is created or not
      conn.close() #closing the connection object
      print("Thanks for using this application")             
