from flask import Flask,request,redirect,render_template,session
import random
app=Flask(__name__)
app.secret_key="123"
@app.route('/')
def index():

    
    return render_template("index.html")

@app.route('/process_money',methods=["POST"])
def money():
    if request.form["findgold"] =='farm':
        goldtemp = random.randrange(10,21)
        session['yourgold'] += goldtemp
        print goldtemp
        string = "Earned " + str(goldtemp) + " gold from the " + str(request.form["findgold"]) + "!<br>"
        session['stuff'] += string
        return render_template("index.html",gold=session['yourgold'],string = session['stuff'])

    elif request.form["findgold"] =='cave':
        goldtemp = random.randrange(5,11)
        session['yourgold'] += goldtemp
        string = "Earned " + str(goldtemp) + " gold from the " + str(request.form["findgold"]) + "!<br>"
        session['stuff'] += string
        return render_template("index.html",gold=session['yourgold'],string = session['stuff'])

    elif request.form["findgold"] =='house':
        goldtemp = random.randrange(2,6)
        session['yourgold'] += goldtemp
        string = "Earned " + str(goldtemp) + " gold from the " + str(request.form["findgold"]) + "!<br>"
        session['stuff'] += string
        return render_template("index.html",gold=session['yourgold'],string = session['stuff'])

    elif request.form["findgold"] =='casino':
        goldtemp = random.randrange(0,51)
        take = random.randrange(1,3)
        print take
        if take == 1:
            session['yourgold'] += goldtemp
            string = "Earned " + str(goldtemp) + " gold from the " + str(request.form["findgold"]) + "!<br>"
        if take ==2:
            session['yourgold'] -= goldtemp
            string = "Lost " + str(goldtemp) + " gold from the " + str(request.form["findgold"]) + "... Ouch...<br>"
        session['stuff'] += string
        return render_template("index.html",gold=session['yourgold'],string = session['stuff'])

    elif request.form["findgold"] =='empty':
        session['yourgold'] = 0
        session['stuff'] = ""
        return render_template("index.html")
    else:
        return "break"


app.run(debug=True)