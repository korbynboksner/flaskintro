from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    html = "<html><body><h1>Welcome!</h1></body></html>"
    return html

@app.route('/welcome/home')
def say_welcome_home():
    html = "<html><body><h1>Welcome home!</h1></body></html>"
    return html

@app.route('/welcome/back')
def say_welcome_back():
    html = "<html><body><h1>Welcome back!</h1></body></html>"
    return html
