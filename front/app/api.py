# Imports §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ MATTHIEU §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
from datetime import date
import pandas as pd
from flask import Flask, request

# API INSTANCE
app = Flask(__name__)

# API
@app.route('/description_form', methods=['GET', 'POST'])
def description_form():
    # POST
    if request.method == 'POST':
        description = request.form.get('description')
        return '''
                  <h1>The description is: {}</h1>
                  <h1>The meaning is: {}</h1>'''.format(description,'model.predict(description)')

    # GET
    return '''
            <form method="POST">
                <div><label>Description: <input type="text" name="description"></label></div>
                <input type="submit" value="Submit">
            </form>'''
@app.route('/', methods=['GET', 'POST'])
def index():
    # POST
    if request.method == 'POST':
        description = request.form.get('description')
        return '''
                  <h1>The description is: {}</h1>
                  <h1>The meaning is: {}</h1>'''.format(description,'model.predict(description)')

    # GET
    return '''
            <form action="/description_form">
                <input type="submit" value="Go to page predict" />
            </form>'''
if __name__ == '__main__':
    app.run(debug=True)