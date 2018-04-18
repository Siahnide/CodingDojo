from flask import Flask,render_template,request,redirect
app= Flask(__name__)

@app.route('/')
def index ():
    return render_template("index.html")

@app.route('/users',methods=['POST'])
def create_user():
    print "Got Post Info"

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print name,location
    return render_template('users.html',name = request.form['name'],location = request.form['location'],language = request.form['language'],comment = request.form['comment'])
app.run(debug=True)
