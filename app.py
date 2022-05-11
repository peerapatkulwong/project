from flask import Flask, render_template, request
import random
app = Flask(__name__, template_folder = 'template')

@app.route("/",methods=['POST','GET'])
def index():
    number = "0123456789"
    num = ""
    if request.method == 'POST':
        length = int(request.form.get('pw'))
        num = "".join(random.sample(number,length))
    return render_template("index.html",cal = num)

if __name__ == "__main__":
    app.run(debug=True)