from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def demo():
    return 'Keep Learning'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return 'add = %d' %num1
if __name__ == '__main__':
    app.run(debug=True)