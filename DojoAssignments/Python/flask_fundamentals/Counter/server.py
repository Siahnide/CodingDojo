from flask import Flask,render_template,redirect,session
app =  Flask(__name__)
app.secret_key = '123'

@app.route('/',methods=["POST"])
def index ():
    session['count'] = 0
    
    return render_template('index.html')

value=0

@app.route('/plus1',methods=["POST"])
def plusone ():
    session['count'] += 1
    return render_template('index.html', value = session['count'])




app.run(debug=True)