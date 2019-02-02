import csv
from flask import Flask
from flask import render_template  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open("RealEstate.csv") as fobj:
        Header=fobj.readline()
        reader = csv.reader(fobj)
        aList = [row for row in reader]
    return render_template('index.html', fobj = aList)
