
from src import app
from fastapi.testclient import TestClient


# status code constants for reusability
SUCCESS_CODE = 200

client = TestClient(app)


def test_google():
    resp = client.get('/google')
    assert resp.status_code == SUCCESS_CODE
