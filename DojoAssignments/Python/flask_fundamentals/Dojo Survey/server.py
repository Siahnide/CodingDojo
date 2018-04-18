# from flask import Flask,render_template,request,redirect
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/users',methods=['POST'])
# def create_user():
#     print "Request accepted"
#     name = request.form['name']
#     location = request.form['location']
#     language = request.form['language']
#     comment = request.textarea['comment']
#     return render_template('users.html',name = request.form['name'],email = request.form['email'])


# app.run(debug=True)

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   print name,location,language,comment
   # redirects back to the '/' route
   return render_template('users.html',name = request.form['name'],location = request.form['location'],language = request.form['language'],comment = request.form['comment'])
app.run(debug=True) # run our server


