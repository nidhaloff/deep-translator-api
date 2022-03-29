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

from typing import Optional, List
from pydantic import BaseModel


class BaseRequest(BaseModel):
    """model for a base request that require a source & target language and a text to translate"""

    source: str = "auto"
    target: str
    text: str


class BaseRequestWithProxies(BaseRequest):
    """model that inherits BaseRequest props and add support for proxies"""

    proxies: Optional[List[str]] = []


class BaseRequestWithApiKey(BaseRequest):
    api_key: str


class GoogleRequest(BaseRequestWithProxies):
    """model for google request"""


class MyMemoryRequest(BaseRequestWithProxies):
    """model for mymemory request"""


class LingueeRequest(BaseRequestWithProxies):
    """model for google request"""

    return_all: Optional[bool] = False


class PonsRequest(BaseRequestWithProxies):
    """model for pons request"""

    return_all: Optional[bool] = False


class QcriRequest(BaseRequestWithApiKey):
    """model for qcri request"""


class YandexRequest(BaseRequestWithApiKey):
    """model for yandex request"""

    source = "en"
    target = "de"


class MicrosoftRequest(BaseRequestWithApiKey):
    """model for microsoft request"""

    region: Optional[str] = None


class DeeplRequest(BaseRequestWithApiKey):
    """model for DeepL request"""

    source = "en"
    target = "de"
    use_free_api: Optional[bool] = True


class LibreRequest(BaseRequest):
    """model for libre request"""

    source = "en"
    target = "es"
    api_key: Optional[str] = None
    use_free_api: Optional[bool] = True
    custom_url: Optional[str] = None


class PapagoRequest(BaseRequest):
    """model for papago request"""

    client_id: Optional[str] = None
    secret_key: Optional[str] = None
