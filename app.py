from flask import Flask, render_template, request
import random
app = Flask(__name__, template_folder = 'template')

@app.route("/",methods=['POST','GET'])
def ran():
    number = "0123456789"
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('pw'))
        password = "".join(random.sample(number,length))
    return render_template("index.html",cal = password)

if __name__ == "__main__":
    app.run(debug=True)