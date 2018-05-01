from flask import Flask,redirect,render_template,session,flash,request
from mysqlconnection import MySQLConnector
import re
import os, binascii # include this at the top of your file
import md5 # imports the md5 module to generate a hash
salt = binascii.b2a_hex(os.urandom(15))

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "password"
mysql = MySQLConnector(app,'walldb')

@app.route('/',methods=["POST","GET"])
def create():
    return render_template("create.html")




@app.route('/try',methods=["POST"])
def tries():
    if len(request.form["email"]) == 0:
        flash('Please enter an email')
        return render_template('login.html')
    if len(request.form["password"]) == 0:
        flash('Please enter a password')
        return render_template('login.html')
    try:
        email = request.form['email']
        password = request.form['password']
        user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
        query_data = {'email': email}
        user = mysql.query_db(user_query, query_data)
        session["active_user"] =  str(user[0]["first_name"] + " " + user[0]["last_name"])
        session["id"] = str(user[0]["id"])
        active_id = session['id']
        active = session["active_user"]
        if len(user) != 0:
            encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_password:
            return redirect('/wall')

        else:
            flash('incorrect email/password')
            return render_template('login.html')
    except:
        flash('incorrect email/password')
        return render_template('login.html')

@app.route('/login',methods=["POST","GET"])
def login():
    return render_template("login.html")




@app.route('/register',methods=['POST'])
def success():
    data = {
        'first_name': request.form['first_name'],
        'last_name':  request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm': request.form['confirm']
    }
    salt =  binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(data["password"] + salt).hexdigest()

    session['active_user'] = data["email"]
    print session["active_user"]
    if any(char.isdigit() for char in data["first_name"]):
        flash("First Name must contain only letters")
        return render_template('create.html')
    if any(char.isdigit() for char in data["last_name"]):
        flash("Last Name must contain only letters")
        return render_template('create.html')
    if len(data["first_name"]) < 2:
        flash("Please enter a Longer First Name")
        return render_template('create.html')
    if len(data["last_name"]) < 2:
        flash("Please enter a Longer Last Name")
        return render_template('create.html')
    if not EMAIL_REGEX.match(data["email"]):
        flash("Invalid email")
        return render_template('create.html')
    if len(data["password"]) < 8:
        flash("Please enter a Longer Password")
        return render_template('create.html')
    if data["password"] != data["confirm"]:
        flash("Passwords do not match")
        return render_template('create.html')

    # query = "INSERT INTO users (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"
    # mysql.query_db(query,data)


    insert_query = "INSERT INTO users (first_name,last_name, email, password, salt) VALUES (:first_name,:last_name, :email, :hashed_pw, :salt)"
    query_data = { 'first_name': data['first_name'],'last_name': data['last_name'], 'email': data['email'], 'hashed_pw': hashed_pw, 'salt': salt}
    mysql.query_db(insert_query, query_data)
    user = mysql.query_db(insert_query, query_data)
  
    active_id = session["id"]
    active = session["active_user"]
    return redirect('/login')

@app.route('/message',methods=["POST"])
def message():
    insert_query = "INSERT INTO messages (message,user_id,created_at) VALUES (:message,:user_id,NOW())"
    query_data = { 'message':request.form['message'],'user_id':session['id']}
    mysql.query_db(insert_query, query_data)
    return redirect('/wall')

@app.route('/comment',methods=["POST"])
def comment():
    insert_query = "INSERT INTO comments (comment,user_id,created_at,message_id) VALUES (:comment,:user_id,NOW(),:post)"
    query_data = { 'comment':request.form['comment'],'user_id':session['id'],'post':request.form['id']}
    mysql.query_db(insert_query, query_data)
    return redirect('/wall')


@app.route('/wall',methods=["POST","GET"])
def lists():
    query = "SELECT messages.id,messages.message,messages.created_at,users.first_name,users.last_name FROM messages LEFT JOIN users ON messages.user_id = users.id "
    msg = mysql.query_db(query)
    query = "SELECT messages.message,users.first_name,users.last_name,comments.comment,comments.message_id FROM messages LEFT JOIN comments ON comments.message_id = messages.id LEFT JOIN users ON users.id= comments.user_id"
    comment = mysql.query_db(query)
    return render_template('wall.html',active = session["active_user"],all_messages = msg,all_comments = comment,active_id=session["id"])
    

app.run(debug=True)



