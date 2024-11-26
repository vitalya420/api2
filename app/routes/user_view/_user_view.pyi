from sanic import Blueprint
from sanic.views import HTTPMethodView

from app.request import APIRequest

user: Blueprint

class UserView(HTTPMethodView):
    @staticmethod
    async def get(request: APIRequest):
        """
        Get authorized user
        """
        pass

    @staticmethod
    async def post(request: APIRequest):
        """
        Create user
        """

    @staticmethod
    async def put(request: APIRequest):
        """
        Update user
        """
