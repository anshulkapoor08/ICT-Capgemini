from flask import Flask  

app = Flask(__name__)  # Creating the Flask class object  

@app.route('/')  # If You Put @ before any Name it becomes a Decorator  
def home():  
    return ("<center><h3>IntraNet For Our Site</h3></center><br>"
            "<a href='https://www.google.com'>Google Link</a><br>"
            "<a href='https://www.microsoft.com'>Link For Microsoft</a>")  

@app.route('/home/<uname>')  # Decorator being Used  
def home1(uname):  
    return (f"<marquee width='100%' size='14' bgcolor='Pink'>"
            f"<font color='Red'>Welcome To Orange</font></marquee><br><br>"
            f"<b><font size='6' color='Orange'>Welcome : {uname}</font></b>")  
@app.route('/sessionend')  # Decorator being Used
def sessionend():  
    return ("<center><h3>Session Ended</h3></center>")
if __name__ == '__main__':  
    app.run(debug=True)  # Runs the Flask app

#By default flask uses port 5000