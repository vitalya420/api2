import sanic_ext.exceptions
from sanic import BadRequest

from app import app


@app.exception(sanic_ext.exceptions.ValidationError)
async def handle_validation_error(_, exc: sanic_ext.exceptions.ValidationError):
    raise BadRequest
