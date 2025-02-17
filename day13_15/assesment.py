from flask import Flask, request

app = Flask(__name__)

@app.route('/rate', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('ItemName')  # Use request.form for POST data
        quntity = request.form.get('qty')
        rates = request.form.get('rate')
        
    else:
         username = request.form.get('uname')  # Use request.form for POST data
         quntity = request.form.get('qty')
         rates = request.form.get('rate')
    
    return f'<h1>quantity is  {int(quntity)*int(rates)}</h1>',401
    

if __name__ == '__main__':
    app.run(debug=True)