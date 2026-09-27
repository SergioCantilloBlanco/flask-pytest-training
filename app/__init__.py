from flask import Flask

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Aprender testing", "completed": False},
    {"id": 2, "title": "Aprender aleman", "completed": False},
]


@app.route("/tasks")
def get_tasks():
    return Flask.jsonify(tasks)