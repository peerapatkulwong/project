from flask import Flask, render_template, request
import turtle
app = Flask(__name__, template_folder = 'template')

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        color = str(request.form.get('co'))
        length = int(request.form.get('le'))
        if length >= 100:
            geo = turtle.Turtle()
            geo.color(color)
            geo.forward(length)
            geo.left(120)
            geo.forward(length)
            geo.left(120)
            geo.forward(length)
            turtle.done()
            return render_template("index.html")
        elif length <= 100:
            return "<p>error</p>"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)