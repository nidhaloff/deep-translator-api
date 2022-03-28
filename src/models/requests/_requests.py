from typing import Optional
from _base import (
    BaseRequest,
    BaseRequestWithApiKey,
    BaseRequestWithProxies,
)


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
