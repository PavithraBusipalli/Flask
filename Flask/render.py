from flask import Flask, render_template

ap = Flask(__name__)

@ap.route('/first')
def first():
    return render_template('first.html')

@ap.route('/second')
def second():
    return render_template('second.html')

@ap.route('/third')
def third():
    return render_template('third.html')

    
if __name__ == '__main__':
    ap.run(debug=True)