"""
request.pyi
"""

from dataclasses import dataclass

from sanic import Request
from typing_extensions import Optional

@dataclass
class RequestContext:
    waits_otp_confirmation: bool
    otp: Optional[object]

class APIRequest(Request):
    """
    Custom API request class that extends the Sanic Request.
    """

    @property
    def jwt_payload(self) -> object:
        pass

    async def get_user(self) -> object:
        pass

    @classmethod
    def make_context(cls) -> RequestContext:
        pass
