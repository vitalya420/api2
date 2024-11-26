from sanic import text, Blueprint
from sanic.views import HTTPMethodView

from app.schemas.user import UserCreate, UserUpdate
from app.utils.validation.graceful import graceful_validation

user = Blueprint("user", url_prefix="/user")


class UserView(HTTPMethodView):
    @staticmethod
    async def get(request):
        return text("get user")

    @staticmethod
    @graceful_validation(UserCreate)
    async def post(request, body):
        return text(f"post user {body.model_dump_json()}")

    @staticmethod
    @graceful_validation(UserUpdate)
    async def put(request):
        return text("update user")


user.add_route(UserView.as_view(), "/")
