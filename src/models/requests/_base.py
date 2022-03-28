from typing import List, Optional
from pydantic import BaseModel


class BaseRequest(BaseModel):
    """model for a base request that require a source & target language and a text to translate"""

    source: str = "auto"
    target: str
    text: str


class BaseRequestWithProxies(BaseRequest):
    """model that inherits BaseRequest props and add support for proxies"""

    proxies: Optional[List[str]] = None


class BaseRequestWithApiKey(BaseRequest):
    api_key: str
