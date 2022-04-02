"""
main module: entry point of the API
"""

import sys
import os

sys.path.insert(0, os.path.abspath("."))

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

from src.models.requests import (
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

from src.models.responses import TranslationResponse
from src.utils import get_translation, get_summary
from src.metadata import title, description, contact, license_info
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn


# API version
__version__ = "0.1.1"

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
    title=title,
    version=__version__,
    description=description,
    contact=contact,
    license_info=license_info,
)


@app.get("/", summary="show SwaggerUI (this page)")
def home():
    """redirect user to the swagger api"""
    return RedirectResponse("/docs")


@app.post(
    f"/{GOOGLE}/", summary=get_summary(GOOGLE), response_model=TranslationResponse
)
def google_translate(r: GoogleRequest):
    """
    Use google translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    - **proxies**: proxies you want to use (optional)
    """
    t = GoogleTranslator(source=r.source, target=r.target, proxies=r.proxies)
    return get_translation(t, r.text)


@app.post(
    f"/{MICROSOFT}/", summary=get_summary(MICROSOFT), response_model=TranslationResponse
)
def microsoft_translate(r: MicrosoftRequest):
    """
    Use microsoft translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    - **api_key**: microsoft translator api key
    """
    t = MicrosoftTranslator(
        source=r.source, target=r.target, region=r.region, api_key=r.api_key
    )
    return get_translation(t, r.text)


@app.post(f"/{DEEPL}/", summary=get_summary(DEEPL), response_model=TranslationResponse)
def deepl_translate(r: DeeplRequest):
    """
    Use deepl translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    - **api_key**: deepl translator api key
    """
    t = DeeplTranslator(
        api_key=r.api_key,
        source=r.source,
        target=r.target,
        use_free_api=r.use_free_api,
    )
    return get_translation(t, r.text)


@app.post(
    f"/{MYMEMORY}/", summary=get_summary(MYMEMORY), response_model=TranslationResponse
)
def mymemory_translate(r: MyMemoryRequest):
    """
    Use mymemory translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    - **proxies**: proxies you want to use (optional)
    """
    t = MyMemoryTranslator(source=r.source, target=r.target, proxies=r.proxies)
    return get_translation(t, r.text)


@app.post(f"/{LIBRE}/", summary=get_summary(LIBRE), response_model=TranslationResponse)
def libre_translate(r: LibreRequest):
    """
    Use libre translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    - **api_key**: libre translator api key (optional)
    """
    t = LibreTranslator(
        api_key=r.api_key,
        source=r.source,
        target=r.target,
        use_free_api=r.use_free_api,
        custom_url=r.custom_url,
    )
    return get_translation(t, r.text)


@app.post(
    f"/{PAPAGO}/", summary=get_summary(PAPAGO), response_model=TranslationResponse
)
def papago_translate(r: PapagoRequest):
    """
    Use papago translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    - **client_id**: client_id from papago
    - **secret_key**: secret_key that can be retrieved from the papago website

    """
    t = PapagoTranslator(
        client_id=r.client_id,
        secret_key=r.secret_key,
        source=r.source,
        target=r.target,
    )
    return get_translation(t, r.text)


@app.post(
    f"/{YANDEX}/", summary=get_summary(YANDEX), response_model=TranslationResponse
)
def yandex_translate(r: YandexRequest):
    """
    Use yandex translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    - **api_key**: yandex translator api key
    """
    t = YandexTranslator(api_key=r.api_key, source=r.source, target=r.target)
    return get_translation(t, r.text)


@app.post(f"/{PONS}/", summary=get_summary(PONS), response_model=TranslationResponse)
def pons_translate(r: PonsRequest):
    """
    Use pons translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    """
    t = PonsTranslator(source=r.source, target=r.target, proxies=r.proxies)
    return get_translation(t, r.text, return_all=r.return_all)


@app.post(
    f"/{LINGUEE}/", summary=get_summary(LINGUEE), response_model=TranslationResponse
)
def linguee_translate(r: LingueeRequest):
    """
    Use linguee translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    """
    t = LingueeTranslator(source=r.source, target=r.target, proxies=r.proxies)
    return get_translation(t, r.text, return_all=r.return_all)


@app.post(f"/{QCRI}/", summary=get_summary(QCRI), response_model=TranslationResponse)
def qcri_translate(r: QcriRequest):
    """
    Use QCRI translator to translate a text

    - **source**: language to translate from
    - **target**: target language to translate to
    - **text**: text you want to translate
    - **api_key**: QCRI translator api key
    """
    t = QcriTranslator(api_key=r.api_key, source=r.source, target=r.target)
    return get_translation(t, r.text)


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", log_level="info")
