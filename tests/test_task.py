from app import app


def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200

def test_get_tasks_length():
    client = app.test_client()
    response = client.get("/tasks")
    assert len(response.get_json()) == 2

def test_get_tasks_content():
    client = app.test_client()
    response = client.get("/tasks")
    data = response.get_json()
    assert data[0]["title"] == "Aprender testing"
