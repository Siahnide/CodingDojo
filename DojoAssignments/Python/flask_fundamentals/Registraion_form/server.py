from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key="123"
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/user', methods=['POST'])
def create_user():
    print "Got Post Info"

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']

    if len(request.form['firstname']) < 1:
        flash("Please enter a First Name")
    
    if len(request.form['lastname']) < 1:
        flash("Please enter a Last Name")
    if any(char.isdigit() for char in firstname):
        flash("First Name must contain only letters")
        return redirect('/')
    if any(char.isdigit() for char in lastname):
        flash("Last Name must contain only letters")
        return redirect('/')
    if len(request.form['email']) < 1:
        flash("Please enter an email")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email")
        return redirect('/')
    if len(request.form['password']) < 1:
        flash("Please enter a passord!")
    if len(request.form['password']) < 8:
        if len(request.form['password']) > 1:
            flash("Password must be at least 8 characters")
            
    if password != confirm:
        flash("Password doesn't match")
        return redirect('/')
    if len(request.form['confirm']) < 1:
        flash("Please confirm your password!")
        return redirect('/')
    
  
      
     
    return render_template('users.html',firstname = request.form['firstname'],lastname = request.form['lastname'],email = request.form['email'],password = request.form['password'])
app.run(debug=True) 


