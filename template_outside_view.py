"""Moving the template code to a separate file.

Mixing Python code with HTML is ugly. Templates usually live in their own
location. By default, flask will look up for templates in a 'templates'
directory living in the same path as the application.

"""

from flask import Flask
from flask import render_template  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open("RealEstate.csv") as fobj:
        header=fobj.readline()
        data = fobj.readlines()
        Street=data[1].split(",")
        Street1=Street[0]
    return render_template('index.html', fobj = data, Street=Street)
