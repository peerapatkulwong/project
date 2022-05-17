from flask import Flask, render_template, request
from turtle import *
import turtle
app = Flask(__name__, template_folder = 'template')

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        length = str(request.form.get('pw'))
        if length == 'triangle':
            geo = turtle.Turtle()
            geo.forward(100)
            geo.left(120)
            geo.forward(100)
            geo.left(120)
            geo.forward(100)
            turtle.done()
            return render_template("index.html")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)