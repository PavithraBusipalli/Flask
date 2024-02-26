from flask import Flask, redirect, url_for

app = Flask(__name__)

# URL Building 
@app.route('/admin')
def admin():
    return '<center>This is Admin</center>'

@app.route('/student')
def student():
    return '<center>This is Student</center>'

@app.route('/staff')
def staff():
    return '<center>This is Staff</center>'

# Here user takes one arg name which is you provide in the url at browser
# first search for user/<name you wish> after that redirect to the specified function name
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'student':
        return redirect(url_for('student'))
    if name == 'staff':
        return redirect(url_for('staff'))

app. config["CACHE_TYPE"] = "null" 
if __name__ == '__main__':
    app.run(debug=True)

