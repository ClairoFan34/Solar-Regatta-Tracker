from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome team!"

@app.route("/about")
def info():
    return "This website was create by Angel Perez on Oct 18 8:57PM, CA time (whatever that is)"