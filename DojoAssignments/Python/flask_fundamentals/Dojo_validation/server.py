from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key="123"
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
  print "Got Post Info"
    
  name = request.form['name']
  
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  print name,location,language,comment
  if len(request.form['name']) < 1:
    flash("Name cannot be empty")
    
  if len(request.form['comment']) > 120:
    flash("Please limit comment to 120 characters or less")
    
  if len(request.form['language']) < 1:
    flash("Please choose a language")
  if len(request.form['location']) < 1:
    flash("Location cannot be empty")
    return redirect('/')
    
  
      
     
  return render_template('users.html',name = request.form['name'],location = request.form['location'],language = request.form['language'],comment = request.form['comment'])
app.run(debug=True) 


