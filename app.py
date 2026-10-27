from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_database():
    connection = sqlite3.connect("tracker.db")
    connection.row_factory = sqlite3.Row
    return connection

subteams = ["Electrical", "Pontoon", "Hydrofoil", "Steering", "Design"]

@app.route("/")
def home():
    connection = get_database()
    tasks = connection.execute("SELECT * FROM tasks ORDER BY due").fetchall()
    connection.close()
    return render_template("index.html", tasks=tasks, subteams=subteams)


@app.route("/about")
def info():
    return "This website was created by Angel Perez on Oct 18 8:57PM, CA time (whatever that is)"