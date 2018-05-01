from flask import Flask,redirect,render_template,session,flash,request
from mysqlconnection import MySQLConnector
import re
import os, binascii # include this at the top of your file
import md5 # imports the md5 module to generate a hash
salt = binascii.b2a_hex(os.urandom(15))

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "password"
mysql = MySQLConnector(app,'registraiondb')

@app.route('/try',methods=["POST"])
def tries():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)
    session["active_user"] =  str(user[0]["first_name"] + " " + user[0]["last_name"])
    active = session["active_user"]
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
    if user[0]['password'] == encrypted_password:
        return render_template("wall.html",active = session["active_user"],all_users = user)
    # this means we have a successful login!
    else:
        return "invalid password!"














# Just in case you would like to know my first attempt.... took me a bit to see that it was very nicely put up in the hashing module.... I looked in the DB communications module for the longest time. xD

    # data = {
    #     'email': request.form['email'],
    #     'password': md5(request.form['password'] + salt)
    # }
    # password = data["password"]
    # return render_template("list.html",password = data["password"])
    # # query = "SELECT * FROM users WHERE EXISTS(SELECT * FROM users WHERE (email = 'request.form['email']' AND password ='request.form['password']'));"
    # query = "SELECT * FROM users WHERE email='" + data['email'] + "'" 
    # x = mysql.query_db(query)
    # hashed_password = md5(password + salt)
    
    # try:
    #     if x[0]["email"] == data["email"] and x[0]["password"] == data["password"]:
    #         session["active_user"] =  str("[" + str(x[0]["id"]) + "] " + x[0]["first_name"] + " " + x[0]["last_name"])
    #         active = session["active_user"]
    #         query = "SELECT * FROM users"
    #         users = mysql.query_db(query)
            # return render_template('list.html',active = session["active_user"],all_users = users)
    # except:
    #     flash("Incorrect Email/Password")
    #     return render_template("login.html")
    # else:
    #     flash("Incorrect Email/Password")
    #     return render_template("login.html")
        


@app.route('/login',methods=["POST"])
def login():
    return render_template("login.html")

@app.route('/create',methods=["POST"])
def create():
    return render_template("create.html")


@app.route('/list')
def lists():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)

    return render_template('list.html',all_users = users)

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
    return redirect('/list')


app.run(debug=True)



