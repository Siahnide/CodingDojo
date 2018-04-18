from flask import Flask,request,render_template,session,redirect
import random
app = Flask(__name__)
app.secret_key="a"

@app.route('/',methods=["POST"])
def start():
    session['count'] = 0
    session['key']=random.randrange(0,101)
    print session['key']
    return render_template("index.html")

@app.route('/try',methods=["POST"])
def number():
    session['count'] = session['count'] + 1
    guess =  int(request.form['guess'])
    key = session['key']
    print key
    print guess
    if guess == key:
        return render_template("yes.html")
    elif guess < key:
        return render_template("small.html")
    elif guess > key:
        return render_template("large.html")

app.run(debug=True)

