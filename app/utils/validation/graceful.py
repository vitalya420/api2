from functools import wraps
from typing import Type, Literal, Callable, Dict, Any, TYPE_CHECKING

from pydantic import BaseModel, ValidationError
from sanic import BadRequest

try:
    from orjson import loads as loads_
except ImportError:
    from json import loads as loads_

if TYPE_CHECKING:
    from app.request.request import APIRequest

ModelType = Type[BaseModel]


def graceful_validation(
    model: ModelType,
    where: Literal["json", "query", "form"] = "json",
    loads: Callable[[str, ...], Dict] = loads_,
):
    """
    Decorator to validate user data against a Pydantic model and return graceful error messages.

    This decorator is useful because the default validation provided by `sanic_ext.validate()`
    does not return user-friendly error messages. Instead, this decorator captures validation
    errors and formats them into a structured response.

    Parameters:
    - model (ModelType): A Pydantic model class that defines the expected structure of the input data.
    - where (Literal["json", "query", "form"], optional): Specifies the source of the data to validate.
      - "json": Data is expected in the request body as JSON (default).
      - "query": Data is expected in the query parameters (not implemented).
      - "form": Data is expected in form data (not implemented).
    - loads (Callable[[str, ...], Dict], optional): A callable that takes a string and returns a dictionary.
      This is used to parse the input data. By default, it uses `orjson.loads` if available, otherwise falls back to `json.loads`.

    Returns:
    - Callable: A wrapped function that performs validation and returns the original function's response
      if validation is successful. If validation fails, it raises a `BadRequest` with a structured error message.

    Raises:
    - BadRequest: If the input data is empty, invalid JSON, or if validation against the Pydantic model fails.
    - NotImplementedError: If the `where` parameter is set to "query" or "form", as those cases are not implemented.

    Example usage:
        @app.route("/user", methods=["POST"])
        @graceful_validation(UserCreate)
        async def create_user(request, body):
            return text(f'User created: {body}')
    """

    def wrapper(f: Callable) -> Callable:
        @wraps(f)
        def decorated(request: "APIRequest", *args, **kwargs) -> Any:
            try:
                if where == "json":
                    result = request.load_json(loads=loads)
                    if result is None:
                        raise BadRequest("Empty JSON")
                    kwargs["body"] = model(**result)
                    return f(request, *args, **kwargs)
                raise NotImplementedError
            except ValidationError as exc:
                errors = {}
                for error in exc.errors():
                    field = error["loc"][-1]
                    message = error["msg"]
                    errors[field] = message
                raise BadRequest(context=errors)

        return decorated

    return wrapper
