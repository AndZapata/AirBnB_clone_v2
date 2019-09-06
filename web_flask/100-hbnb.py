#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def states_hbnb():
    ''' display “states HBNB!” '''
    list_state = list(storage.all("State").values())
    list_amenity = list(storage.all("Amenity").values())
    list_place = list(storage.all("Place").values())
    list_user = list(storage.all("User").values())
    return render_template('100-hbnb.html',
                           list_state=list_state, list_amenity=list_amenity,
                           list_place=list_place, list_user=list_user)


@app.teardown_appcontext
def state_close(error):
    ''' close the session '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
