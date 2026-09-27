from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Aprender testing", "completed": False},
    {"id": 2, "title": "Aprender aleman", "completed": False},
]


@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400
    new_task = {"id": len(tasks)+1, "title": title, "completed":False}
    tasks.append(new_task)
    return jsonify(new_task), 201