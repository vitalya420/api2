from sanic import Sanic

from app.request.request import APIRequest
from app.routes import test_bp
from app.routes.mobile import mobile_api
from app.routes.user_view import user

app = Sanic("my_app", request_class=APIRequest)
app.blueprint([test_bp, mobile_api, user])

from . import exceptions
