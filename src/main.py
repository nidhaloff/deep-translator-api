# Copyright 2022 Nidhal Baccouri
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
from metadata import title, description, contact, license_info
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
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
    title=title,
    version=__version__,
    description=description,
    contact=contact,
    license_info=license_info,
)


@app.get("/", summary="show SwaggerUI (this page)")
def home():
    return RedirectResponse("/docs")


@app.post(
    f"/{GOOGLE}/", summary=get_summary(GOOGLE), response_model=TranslationResponse
)
def google_translate(r: GoogleRequest):
    t = GoogleTranslator(source=r.source, target=r.target, proxies=r.proxies)
    return get_translation(t, r.text)


@app.post(
    f"/{MICROSOFT}/", summary=get_summary(MICROSOFT), response_model=TranslationResponse
)
def microsoft_translate(r: MicrosoftRequest):
    t = MicrosoftTranslator(
        source=r.source,
        target=r.target,
        region=r.region,
        proxies=r.proxies,
    )
    return get_translation(t, r.text)


@app.post(f"/{DEEPL}/", summary=get_summary(DEEPL), response_model=TranslationResponse)
def deepl_translate(r: DeeplRequest):
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
    t = MyMemoryTranslator(source=r.source, target=r.target, proxies=r.proxies)
    return get_translation(t, r.text)


@app.post(f"/{LIBRE}/", summary=get_summary(LIBRE), response_model=TranslationResponse)
def libre_translate(r: LibreRequest):
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
    t = YandexTranslator(api_key=r.api_key, source=r.source, target=r.target)
    return get_translation(t, r.text)


@app.post(f"/{PONS}/", summary=get_summary(PONS), response_model=TranslationResponse)
def pons_translate(r: PonsRequest):
    t = PonsTranslator(source=r.source, target=r.target, proxies=r.proxies)
    return get_translation(t, r.text, return_all=r.return_all)


@app.post(
    f"/{LINGUEE}/", summary=get_summary(LINGUEE), response_model=TranslationResponse
)
def linguee_translate(r: LingueeRequest):
    t = LingueeTranslator(source=r.source, target=r.target, proxies=r.proxies)
    return get_translation(t, r.text, return_all=r.return_all)


@app.post(f"/{QCRI}/", summary=get_summary(QCRI), response_model=TranslationResponse)
def qcri_translate(r: QcriRequest):
    t = QcriTranslator(api_key=r.api_key, source=r.source, target=r.target)
    return get_translation(t, r.text)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="info")
