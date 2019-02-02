"""Moving the template code to a separate file.

Mixing Python code with HTML is ugly. Templates usually live in their own
location. By default, flask will look up for templates in a 'templates'
directory living in the same path as the application.

"""
import pymysql
from flask import Flask
from flask import render_template  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    db=pymysql.connect(host="localhost",port=3306,user="root",passwd="MySQLRoot",db="schlumberger")
    cursor=db.cursor()
    sql="""select * from empdb"""
    data=cursor.execute(sql)
    row = cursor.fetchall()
    db.close()
    return render_template('index.html', authors = row)
