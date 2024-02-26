from flask import Flask,request,render_template

app = Flask(__name__)


'''
@app.route('/login',methods = ['GET'])
def login():

    uname = request.args.get('uname')
    password = request.args.get('pass')
    if uname == 'pavi' and password == 'google':
        return 'welcome %s' %uname
    else:
        return 'invalid %s' %uname

'''

@app.route('/login',methods = ["POST","GET"])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        password = request.form['pass']
        if uname == 'pavi' and password == 'google':
            return '<center>welcome %s</center>' %uname
        else:
            return '<center>%s is invalid</center>' %uname
    return render_template('forms.html')
    


if __name__ == '__main__':
    app.run(debug=True)

