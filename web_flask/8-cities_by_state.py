#!/usr/bin/python3
"""Flask web application """

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ renders a HTML page with a list of states and related cities """
    states = storage.all("State")
    return render_template('8-cities_by_state.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the storage on teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
