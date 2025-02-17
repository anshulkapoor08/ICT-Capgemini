from flask import Flask, request
app = Flask(__name__)  # Creating the Flask class object

@app.route('/login', methods= ['GET','POST'])  # If You Put @ before any Name it becomes a Decorator

def login():
    username = request.args.get('uname')    
    password = request.args.get('pass')
    
    if username == 'admin' and password == 'kapoor':
        return ("<B> Welcome Admin %s</B>"%username   )

if __name__ == '__main__':  
    app.run(debug=True)  # Runs the Flask app    