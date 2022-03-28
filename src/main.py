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
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return "Server is running. Go to /docs to try out the API"


@app.post("/google/")
def google_translate(request: GoogleRequest):
    t = GoogleTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return {"translation": t.translate(text=request.text)}


@app.post("/microsoft/")
def microsoft_translate(request: MicrosoftRequest):
    t = MicrosoftTranslator(
        source=request.source,
        target=request.target,
        region=request.region,
        proxies=request.proxies,
    )
    return {"translation": t.translate(text=request.text)}


@app.post("/deepl/")
def deepl_translate(request: DeeplRequest):
    t = DeeplTranslator(
        api_key=request.api_key,
        source=request.source,
        target=request.target,
        use_free_api=request.use_free_api,
    )
    return {"translation": t.translate(text=request.text)}


@app.post("/mymemory/")
def mymemory_translate(request: MyMemoryRequest):
    t = MyMemoryTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return {"translation": t.translate(text=request.text)}


@app.post("/libre/")
def libre_translate(request: LibreRequest):
    t = LibreTranslator(
        api_key=request.api_key,
        source=request.source,
        target=request.target,
        use_free_api=request.use_free_api,
        custom_url=request.custom_url,
    )
    return {"translation": t.translate(text=request.text)}


@app.post("/papago/")
def papago_translate(request: PapagoRequest):
    t = PapagoTranslator(
        client_id=request.client_id,
        secret_key=request.secret_key,
        source=request.source,
        target=request.target,
    )
    return {"translation": t.translate(text=request.text)}


@app.post("/yandex/")
def yandex_translate(request: YandexRequest):
    t = YandexTranslator(
        api_key=request.api_key, source=request.source, target=request.target
    )
    return {"translation": t.translate(text=request.text)}


@app.post("/pons/")
def pons_translate(request: PonsRequest):
    t = PonsTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return {
        "translation": t.translate(word=request.text, return_all=request.return_all)
    }


@app.post("/linguee/")
def linguee_translate(request: LingueeRequest):
    t = LingueeTranslator(
        source=request.source, target=request.target, proxies=request.proxies
    )
    return {
        "translation": t.translate(word=request.text, return_all=request.return_all)
    }


@app.post("/qcri/")
def qcri_translate(request: QcriRequest):
    t = QcriTranslator(
        api_key=request.api_key, source=request.source, target=request.target
    )
    return {"translation": t.translate(text=request.text)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
