#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_hbnb():
    ''' display “states HBNB!” '''
    list_state = list(storage.all("State").values())
    return render_template('8-cities_by_states.html', list_state=list_state)


@app.teardown_appcontext
def state_close(error):
    ''' close the session '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
