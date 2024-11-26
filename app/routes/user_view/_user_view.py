from sanic import text, Blueprint
from sanic.views import HTTPMethodView

user = Blueprint('/user', url_prefix='/user')


class UserView(HTTPMethodView):
    @staticmethod
    async def get(request):
        return text('get user')

    @staticmethod
    async def post(request):
        return text('create user')

    @staticmethod
    async def put(request):
        return text('update user')


user.add_route(UserView.as_view(), '/')
