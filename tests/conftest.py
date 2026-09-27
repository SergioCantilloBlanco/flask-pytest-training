import pytest
from app import app
import app as a

@pytest.fixture
def initial_tasks():
    return[
    {"id": 1, "title": "Aprender testing", "completed": False},
    {"id": 2, "title": "Aprender aleman", "completed": False},]

@pytest.fixture
def reset_tasks(initial_tasks):
    a.tasks = initial_tasks.copy()


@pytest.fixture
def client(reset_tasks):
    client = app.test_client()

    yield client