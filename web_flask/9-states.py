#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_hbnb(id=None):
    ''' display “states HBNB!” '''
    dict_state = storage.all("State")
    list_state = list(dict_state.values())
    if id is not None:
        key = 'State.{}'.format(id)
        if key in dict_state:
            list_state = [dict_state[key]]
    return render_template('9-states.html',
                           list_state=list_state, id=id)


@app.teardown_appcontext
def state_close(error):
    ''' close the session '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
