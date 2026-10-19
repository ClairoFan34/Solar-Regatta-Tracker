from flask import Flask, render_template

app = Flask(__name__)

tasks = [
    {"title": "Wire battery to motor controller", "owner": "Ana", "subteam": "Electrical", "due": "2026-10-30", "status": "in progress"},
    {"title": "Figure out the steering connection", "owner": "Angel", "subteam": "Electrical", "due": "2026-11-21", "status": "in progress"},
    {"title": "Seal pontoon seams", "owner": "Luis", "subteam": "Pontoon", "due": "2026-11-05", "status": "to do"},
    {"title": "Test hydrofoil angle", "owner": "Sofia", "subteam": "Hydrofoil", "due": "2026-10-25", "status": "to do"},
    {"title": "Mount steering cable", "owner": "Diego", "subteam": "Steering", "due": "2026-11-01", "status": "done"},
    {"title": "Finalize hull paint design", "owner": "Maya", "subteam": "Design", "due": "2026-11-08", "status": "in progress"},
]
subteams = ["Electrical", "Pontoon", "Hydrofoil", "Steering", "Design"]

@app.route("/")
def home():
    return render_template("index.html", tasks = tasks, subteams = subteams)

@app.route("/about")
def info():
    return "This website was create by Angel Perez on Oct 18 8:57PM, CA time (whatever that is)"