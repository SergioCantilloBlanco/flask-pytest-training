from app import app
import pytest

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
    assert data == {"id":3, "title":"Aprender mocks", "completed":False}


@pytest.mark.parametrize("datos", [{},{"title": "   "},{"title": None}, {"title": ""}])
def test_create_task_whitespace_title(client, datos):
    response = client.post("/tasks", json=datos)
    data = response.get_json()
    assert response.status_code == 400
    assert data == {"error": "Title is required"}

def test_create_task_adds_task(client):
    response = client.get("/tasks")
    num_initial_res = len(response.get_json())
    client.post("/tasks",  json={"title": "Aprender mocks"})
    response = client.get("/tasks")
    tasks = response.get_json()
    num_posted_titles = len(response.get_json())
    assert num_posted_titles == num_initial_res + 1
    assert tasks[-1]["title"] == "Aprender mocks"

def test_initial_tasks(client, initial_tasks):
    response = client.get("/tasks")
    assert len(response.get_json()) == len(initial_tasks)



