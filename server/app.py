#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    count = f''
    for x in range(parameter):
        count += f'{x}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == "+":
        return str(num1 + num2) 
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation.lower() == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    else:
        raise ValueError("Operation must be a valid operator")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
