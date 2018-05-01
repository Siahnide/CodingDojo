from flask import Flask,redirect,render_template,session,flash,request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "password"
mysql = MySQLConnector(app,'semirestdb')


@app.route("/",methods=["Post","GET"])
def index():
    query = "SELECT * FROM users"
    mysql.query_db(query)
    all_users = mysql.query_db(query)
    return render_template('index.html',all_users=mysql.query_db(query))


@app.route('/create',methods=["GET","POST"])
def create():
    return render_template("create.html")

@app.route('/try',methods=["POST"])
def tries():
    query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW());"
    data={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "created":"NOW()"
    }
    # query = "INSERT INTO users ('first_name', 'last_name', 'email', 'created_at') VALUES (:first_name,:last_name,:email,:created);"
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/users',methods=["POST"])
def users():
    session["active"] = request.form["id"]
    active={"active":session["active"]}
    query = "SELECT * FROM users WHERE id = :active"
    user = mysql.query_db(query,active)
    return render_template("users.html",user = mysql.query_db(query,active))

@app.route('/edit',methods=["POST"])
def edit():
    session["active"] = request.form["id"]
    active={"active":session["active"]}
    query = "SELECT * FROM users WHERE id = :active"
    user = mysql.query_db(query,active)
    return render_template("edit.html",user = mysql.query_db(query,active))

@app.route('/tryedit',methods=["POST"])
def tryedit():
    session["active"] = request.form["id"]

    data={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "active":session["active"]
    }
    query = "UPDATE users SET first_name=:first_name,last_name=:last_name,email=:email,created_at=NOW() WHERE users.id=:active"
    mysql.query_db(query,data)
    query = "SELECT * FROM users"

    return render_template("index.html",all_users=mysql.query_db(query,data))

@app.route('/trydel',methods=["POST"])
def trydel():
    session["active"] = request.form["id"]

    data={
        "active":session["active"]
    }
    query = "DELETE FROM users WHERE id=:active;"
    mysql.query_db(query,data)
    query = "SELECT * FROM users"

    return render_template("index.html",all_users=mysql.query_db(query,data))

app.run(debug=True)