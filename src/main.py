from deep_translator import (
    GoogleTranslator,
    MicrosoftTranslator,
    PonsTranslator,
    LingueeTranslator,
    LibreTranslator,
    MyMemoryTranslator,
    YandexTranslator,
    PapagoTranslator,
    DeeplTranslator,
    QcriTranslator,
)

from models.requests import (
    MicrosoftRequest,
    GoogleRequest,
    DeeplRequest,
    LibreRequest,
    LingueeRequest,
    PapagoRequest,
    PonsRequest,
    YandexRequest,
    MyMemoryRequest,
    QcriRequest,
)

from models.responses import TranslationResponse
from utils import get_translation
from fastapi import FastAPI
import uvicorn

__version__ = "0.1.0"

app = FastAPI(
    title="deep-translator API",
    version=__version__,
    description="Official deep-translator API",
)


@app.get("/")
async def root():
    return "Server is running. Go to /docs to try out the API"


@app.post("/google/", response_model=TranslationResponse)
def google_translate(request: GoogleRequest):
    t = GoogleTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return get_translation(t, request.text)


@app.post("/microsoft/", response_model=TranslationResponse)
def microsoft_translate(request: MicrosoftRequest):
    t = MicrosoftTranslator(
        source=request.source,
        target=request.target,
        region=request.region,
        proxies=request.proxies,
    )
    return get_translation(t, request.text)


@app.post("/deepl/", response_model=TranslationResponse)
def deepl_translate(request: DeeplRequest):
    t = DeeplTranslator(
        api_key=request.api_key,
        source=request.source,
        target=request.target,
        use_free_api=request.use_free_api,
    )
    return get_translation(t, request.text)


@app.post("/mymemory/", response_model=TranslationResponse)
def mymemory_translate(request: MyMemoryRequest):
    t = MyMemoryTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return get_translation(t, request.text)


@app.post("/libre/", response_model=TranslationResponse)
def libre_translate(request: LibreRequest):
    t = LibreTranslator(
        api_key=request.api_key,
        source=request.source,
        target=request.target,
        use_free_api=request.use_free_api,
        custom_url=request.custom_url,
    )
    return get_translation(t, request.text)


@app.post("/papago/", response_model=TranslationResponse)
def papago_translate(request: PapagoRequest):
    t = PapagoTranslator(
        client_id=request.client_id,
        secret_key=request.secret_key,
        source=request.source,
        target=request.target,
    )
    return get_translation(t, request.text)


@app.post("/yandex/", response_model=TranslationResponse)
def yandex_translate(request: YandexRequest):
    t = YandexTranslator(
        api_key=request.api_key, source=request.source, target=request.target
    )
    return get_translation(t, request.text)


@app.post("/pons/", response_model=TranslationResponse)
def pons_translate(request: PonsRequest):
    t = PonsTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return get_translation(t, request.text, return_all=request.return_all)


@app.post("/linguee/", response_model=TranslationResponse)
def linguee_translate(request: LingueeRequest):
    t = LingueeTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return get_translation(t, request.text, return_all=request.return_all)


@app.post("/qcri/", response_model=TranslationResponse)
def qcri_translate(request: QcriRequest):
    t = QcriTranslator(
        api_key=request.api_key, source=request.source, target=request.target
    )
    return get_translation(t, request.text)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
