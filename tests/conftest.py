import pytest
from app import app
import app as a


@pytest.fixture
def client():
    a.tasks = [
    {"id": 1, "title": "Aprender testing", "completed": False},
    {"id": 2, "title": "Aprender aleman", "completed": False},]
    client = app.test_client()

    yield client