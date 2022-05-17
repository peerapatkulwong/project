from flask import Flask, render_template, request
from turtle import *
import turtle
app = Flask(__name__, template_folder = 'template')

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        length = int(request.form.get('pw'))
        if length >= 100:
            geo = turtle.Turtle()
            geo.forward(100)
            geo.left(120)
            geo.forward(100)
            geo.left(120)
            geo.forward(100)
            turtle.done()
            return render_template("index.html")
        elif length <= 100:
            return '<p>error</p>'
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)