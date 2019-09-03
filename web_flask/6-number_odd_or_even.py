#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' display “Hello HBNB!” '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' display “HBNB” '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    ''' display “HBNB” '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_is_cool(text='is_cool'):
    ''' display “HBNB” '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    ''' display “N” '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    ''' display “N” '''
    return '{}'.format(render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd_or_even(n):
    ''' display “N, odd|even” '''
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, mod='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, mod='odd')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
