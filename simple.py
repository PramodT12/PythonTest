from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Our Library!'

@app.route('/app1')
def hello_world1():
    return 'Welcome to App1 Library!'
