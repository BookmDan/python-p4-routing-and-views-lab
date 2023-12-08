#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<p>Printed String: {param}</p>'

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(1, param+1))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation'

    return f'<p>Result of {num1} {operation} {num2} is: {result}</p>'

if __name__ == '__main__':
    app.run(port=8003, debug=True)
print("hello")