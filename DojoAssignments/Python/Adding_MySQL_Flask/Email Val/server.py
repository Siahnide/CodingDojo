from flask import Flask, request,redirect,render_template,session,flash

from mysqlconnection import MySQLConnector
app = Flask(__name__)
import re
app.secret_key="123"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mysql = MySQLConnector(app, 'emaildb')

@app.route('/')
def index():
   
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('index.html',all_emails = emails)


@app.route('/create_email',methods = ["POST"])
def create():
    if len(request.form['email']) < 1:
        flash("Please enter an email")
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email")
        return redirect('/')
    else:
        flash(("The email address you entered " + request.form['email'] + " is a VALID email address! Thankyou!"))
        query = "INSERT INTO emails (name, created_at, updated_at) VALUES (:email_name, NOW(), NOW())"
        data = {
                'email_name':request.form['email']
                }
        mysql.query_db(query, data)
        return redirect('/')

app.run(debug=True)
