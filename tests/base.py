from fastapi import Response
from src.main import app
from fastapi.testclient import TestClient
from tests.data import j, j_with_api


client = TestClient(app)


class Base:
    def __init__(self, req: str = j):
        self.resp = client.post(f"/{self.translator}/", json=req)
