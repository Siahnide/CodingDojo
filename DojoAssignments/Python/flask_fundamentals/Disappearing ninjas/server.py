from flask import Flask,render_template,redirect

app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<color>')
def tmnt (color):
    if color=='blue':
        return render_template("blue.html")
    if color=='orange':
        return render_template("orange.html")
    if color=='red':
        return render_template("red.html")
    if color=='purple':
        return render_template("purple.html")
    else:
        return render_template("not.html")


app.run(debug=True)