#You have to input the IP Address of a server
#the output will show all the octats separately
import ipaddress
try:
    ipadd = ipaddress.ip_address(input("Enter the IP Address : ").strip())
    words = str(ipadd).split(".")
    print("No of octats is : ", len(words))
    for x in words:
        print(x)
except ValueError:
    print("Invalid IP Address")
except Exception as e:
    print("all good : ", e)  
finally:
    print("thanks for visiting64")      
    