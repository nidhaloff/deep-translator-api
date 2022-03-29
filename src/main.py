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
from utils import get_translation, get_summary
from fastapi import FastAPI
import uvicorn

# API version
__version__ = "0.1.0"

# Constants for reusability as an endpoint and in the summary docs
GOOGLE = "google"
MICROSOFT = "microsoft"
MYMEMORY = "mymemory"
LIBRE = "libre"
DEEPL = "deepl"
QCRI = "qcri"
YANDEX = "yandex"
PONS = "pons"
PAPAGO = "papago"
LINGUEE = "linguee"

# app object
app = FastAPI(
    title="deep-translator API",
    version=__version__,
    description="""
    Official deep-translator API. Get multiple translations from multiple sources/translators
    including google, msft, mymemory, libre, etc..

    This API is based on the deep-translator python package (https://github.com/nidhaloff/deep-translator).
    """,
)


@app.get("/", summary="root query just for testing purposes at the moment")
async def root():
    return "Server is running. Go to /docs to try out the API"


@app.post(
    f"/{GOOGLE}/", summary=get_summary(GOOGLE), response_model=TranslationResponse
)
def google_translate(request: GoogleRequest):
    t = GoogleTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return get_translation(t, request.text)


@app.post(
    f"/{MICROSOFT}/", summary=get_summary(MICROSOFT), response_model=TranslationResponse
)
def microsoft_translate(request: MicrosoftRequest):
    t = MicrosoftTranslator(
        source=request.source,
        target=request.target,
        region=request.region,
        proxies=request.proxies,
    )
    return get_translation(t, request.text)


@app.post(f"/{DEEPL}/", summary=get_summary(DEEPL), response_model=TranslationResponse)
def deepl_translate(request: DeeplRequest):
    t = DeeplTranslator(
        api_key=request.api_key,
        source=request.source,
        target=request.target,
        use_free_api=request.use_free_api,
    )
    return get_translation(t, request.text)


@app.post(
    f"/{MYMEMORY}/", summary=get_summary(MYMEMORY), response_model=TranslationResponse
)
def mymemory_translate(request: MyMemoryRequest):
    t = MyMemoryTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return get_translation(t, request.text)


@app.post(f"/{LIBRE}/", summary=get_summary(LIBRE), response_model=TranslationResponse)
def libre_translate(request: LibreRequest):
    t = LibreTranslator(
        api_key=request.api_key,
        source=request.source,
        target=request.target,
        use_free_api=request.use_free_api,
        custom_url=request.custom_url,
    )
    return get_translation(t, request.text)


@app.post(
    f"/{PAPAGO}/", summary=get_summary(PAPAGO), response_model=TranslationResponse
)
def papago_translate(request: PapagoRequest):
    t = PapagoTranslator(
        client_id=request.client_id,
        secret_key=request.secret_key,
        source=request.source,
        target=request.target,
    )
    return get_translation(t, request.text)


@app.post(
    f"/{YANDEX}/", summary=get_summary(YANDEX), response_model=TranslationResponse
)
def yandex_translate(request: YandexRequest):
    t = YandexTranslator(
        api_key=request.api_key, source=request.source, target=request.target
    )
    return get_translation(t, request.text)


@app.post(f"/{PONS}/", summary=get_summary(PONS), response_model=TranslationResponse)
def pons_translate(request: PonsRequest):
    t = PonsTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return get_translation(t, request.text, return_all=request.return_all)


@app.post(
    f"/{LINGUEE}/", summary=get_summary(LINGUEE), response_model=TranslationResponse
)
def linguee_translate(request: LingueeRequest):
    t = LingueeTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return get_translation(t, request.text, return_all=request.return_all)


@app.post(f"/{QCRI}/", summary=get_summary(QCRI), response_model=TranslationResponse)
def qcri_translate(request: QcriRequest):
    t = QcriTranslator(
        api_key=request.api_key, source=request.source, target=request.target
    )
    return get_translation(t, request.text)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="info")
