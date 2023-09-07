from flask import Flask
 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<text>')
def print_text(text):
    print(text)
    return text

@app.route('/count/<int:num>')
def count(num):
    count = ''
    for i in range(num):
        count += str(i) + '\n'
    return count
@app.route('/math/<int:a>/<op>/<int:b>')
def math(a, op, b):
    if op == '+':
        return str(a + b)
    elif op == '-':
        return str(a - b)
    elif op == '*':
        return str(a * b)
    elif op == 'div':
        return str(a / b)
    elif op == '%':
        return str(a % b)
        
if __name__ == '__main__':
    app.run(debug=True)