from flask import Flask,render_template
app=Flask(__name__) #creating the Flask class object   

@app.route('/') #If You Put @ before any Name it becomes a Decorator 
def home():
    return ("<Center><H3>IntraNet For Our Site</Center></H3><BR><A Href=https://www.google.com>Google Link</A><BR><A Href=https://www.Microsoft.com>Link For Microsoft</A>")

@app.route('/home/<uname>') #Decorator being Used 
def home1(uname):
    return ("<Marquee width=100% Size=14 BgColor=Pink><Font Color=Red>Welcome To Orange</Font></Marquee><Br><Br><B><Font Size=6 Color=Orange>Welcome : "+uname+"</Font></B>")
@app.route('/sessionend')
def endofsession():
    return("<B> this is the end of session</B>")
@app.route('/course')
def course():
    return render_template('akgec.html')
@app.route('/movie')
def movie():
    return render_template('movies.html')
if __name__=='__main__':
    #app.run(port=7000,debug=True)
    app.run(debug=True)