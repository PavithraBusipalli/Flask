from flask import Flask, render_template

app = Flask(__name__)

@app.route('/msg/<name>')
def msg(name):
    return render_template('msg.html',name=name)

@app.route('/stylesheet')
def stylesheet():
    return render_template('style.html')

if __name__ == '__main__':
    app.run(debug=True)
