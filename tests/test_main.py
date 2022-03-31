


from src.main import app
from fastapi.testclient import TestClient
from tests.data import j, j_with_api


# status code constants for reusability
SUCCESS_CODE = 200

client = TestClient(app)


def get_translator_resp(translator: str, json: str = j):
    resp = client.post(f'/{translator}/', json=json)
    return resp.status_code


def test_google():
    assert get_translator_resp('google') == SUCCESS_CODE

def test_mymemory():
    assert get_translator_resp('mymemory') == SUCCESS_CODE
def test_pons():
    assert get_translator_resp('pons') == SUCCESS_CODE
def test_linguee():
    assert get_translator_resp('linguee') == SUCCESS_CODE
def test_qcri():
    assert get_translator_resp('qcri', j_with_api) == SUCCESS_CODE

def test_microsoft():
    assert get_translator_resp('microsoft', j_with_api) == SUCCESS_CODE

def test_deepl():
    assert get_translator_resp('deepl', j_with_api) == SUCCESS_CODE

def test_libre():
    assert get_translator_resp('libre', j_with_api) == SUCCESS_CODE

def test_yandex():
    assert get_translator_resp('yandex', j_with_api) == SUCCESS_CODE
