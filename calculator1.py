from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def calculator():
    return render_template('calculator.html')

@app.route('/calculator',methods=['POST'])
def results():
    return render_template("calculator.html",
    calc=eval(request.form['op1']+ request.form['operator']+ request.form['op2'] ))


if __name__ == "__main__":
    app.run(debug=True)