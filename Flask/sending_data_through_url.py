from flask import Flask

app = Flask(__name__)

@app.route('/send_str/<name>')
def send(name):
    return 'Hi There, I am string: '+name

@app.route('/send_num/<int:num>')
def numm(num):
    return 'Hi There, I am a number: '+str(num)

@app.route('/send_float/<float:floatnum>')
def send_float(floatnum):
    return 'Hi There, who is there'+' '+str(floatnum)

if __name__=='__main__':
    app.run(debug=True)