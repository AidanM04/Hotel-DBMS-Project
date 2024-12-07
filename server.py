from flask import Flask, render_template, request
from roomdata import get_query_result, add_to_table, update_in_table, delete_from_table
from login import testlogin
from databasedirector import direct_with_args
from waitress import serve
from json import loads

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/adminlogin')
def login():
    return render_template('adminlogin.html')


@app.route('/databaseAccess')
def login_test():
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


@app.route('/adminAccess')
def back_to_entry_form():
    return render_template("databaseAccess.html")


@app.route('/directByInputs')
def view_data_director():
    # Requests data input into 'crudForm' last
    crudfunction = request.args.get('menusName')
    selectedtable = request.args.get('subMenusName')
    whateverID = request.args.get('somethingID')
    #print(crudfunction, selectedtable, whateverID)

    direction_result = direct_with_args(crudfunction, selectedtable, whateverID)
    #print(direction_result)

    if direction_result == 'failed':
        return render_template("accessfailed.html")
    
    # These functions, are the next thing to work on
    elif direction_result[0] == 'get':
        API_result = get_query_result(direction_result[1])
        action = 'Read'
        return render_template("databaseView.html", API_result = API_result, action = action)

    elif direction_result[0] == 'delete':
        API_result = delete_from_table(direction_result[1], direction_result[2])
        action = 'Delete'
        return render_template("databaseView.html", API_result = API_result, action = action)

    elif direction_result[0] == 'post':
        action = 'Create'
        true_action = direction_result[0]
        table = direction_result[1]
        return render_template("databaseInput.html", action = action, true_action = true_action, table = table)

    elif direction_result[0] == 'put':
        action = 'Update'
        true_action = direction_result[0]
        table = direction_result[1]
        item_id = direction_result[2]
        return render_template("databaseInput.html", action = action, true_action = true_action, table = table, item_id = item_id)


@app.route('/databaseAddUpdate')
def add_update_data():

    # vars for database interations
    crudfunction = request.args.get('cuChoice')
    selectedtable = request.args.get('funcChoice')
    whateverID = request.args.get('idForUpdate')
    inputjson = request.args.get('json_to_send')

    inputjsondict = loads(inputjson)

    action = request.args.get('crudAction')

    if crudfunction == 'post':
        API_result = add_to_table(selectedtable, inputjsondict)
        return render_template("databaseView.html", API_result = API_result, action = action)


    elif crudfunction == 'put':
        API_result = update_in_table(selectedtable, whateverID, inputjsondict)
        return render_template("databaseView.html", API_result = API_result, action = action)





if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 9000)
