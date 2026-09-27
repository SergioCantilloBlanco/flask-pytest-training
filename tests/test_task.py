from app import app

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200

def test_get_tasks_length(client):
    response = client.get("/tasks")
    assert len(response.get_json()) == 2

def test_get_tasks_content(client):
    response = client.get("/tasks")
    data = response.get_json()
    assert data[0]["title"] == "Aprender testing"

def test_create_task_status(client):
    response = client.post("/tasks",  json={"title": "Aprender mocks"})
    assert response.status_code == 201

def test_create_task_content(client):
    response = client.post("/tasks", json={"title": "Aprender mocks"})
    data = response.get_json()
    assert data == {"id":4, "title":"Aprender mocks", "completed":False}

def test_create_task_without_title(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400



