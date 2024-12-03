from flask import Flask, render_template, request
from roomdata import get_query_result, add_to_table, update_in_table, delete_from_table
from login import testlogin
from databasedirector import direct_with_args
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

@app.route('/directByInputs')
def viewdatadirector():
    # Requests data input into 'crudForm' last
    crudfunction = request.args.get('menusName')
    selectedtable = request.args.get('subMenusName')
    whateverID = request.args.get('somethingID')

    direction_result = direct_with_args(crudfunction, selectedtable, whateverID)

    if direction_result == 'failed':
        return render_template("accessfailed.html")
    
    # These functions, are the next thing to work on
    elif direction_result[0] == 'get':
        database_read = get_query_result(direction_result[1])

    elif direction_result[0] == 'delete':
        database_delete = delete_from_table(direction_result[1], direction_result[2])

    elif direction_result[0] == 'post':

    elif direction_result[0] == 'put':

    




if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 9000)
