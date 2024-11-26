from sanic import Blueprint
from sanic.views import HTTPMethodView

from app.request import APIRequest
from app.schemas.user import UserCreate

user: Blueprint

class UserView(HTTPMethodView):
    @staticmethod
    async def get(request: APIRequest):
        """
        Get authorized user
        """
        pass

    @staticmethod
    async def post(request: APIRequest, body: UserCreate):
        """
        Create user
        """

    @staticmethod
    async def put(request: APIRequest):
        """
        Update user
        """
