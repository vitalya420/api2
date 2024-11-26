from sanic import Blueprint, text, NotFound

from app.request.request import APIRequest
from app.services.user import UserService

test_bp = Blueprint("test")


@test_bp.route("/")
async def index(request: APIRequest):
    return text("hello. how are you?")
