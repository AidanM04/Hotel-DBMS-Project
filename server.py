from flask import Flask, render_template, request
from roomdata import get_query_result
from login import testlogin
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/adminlogin')
def login():
    return render_template('adminlogin.html')


@app.route('/databaseAccess')
def logintest():
    usern = request.args.get('username')
    passw = request.args.get('password')

# Check for empty strings / line with only spaces
    if not bool(usern.strip()):
        usern = "NaN"

    if not bool(passw.strip()):
        passw = "NaN"

    loginresult = testlogin(usern, passw)
    if loginresult == False:
        return render_template("loginfailed.html")
    
    return render_template("databaseAccess.html")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 9000)
