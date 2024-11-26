from sanic import Request


class APIRequest(Request):
    def __init__(self, *sanic_args, **sanic_kwargs):
        super().__init__(*sanic_args, **sanic_kwargs)
