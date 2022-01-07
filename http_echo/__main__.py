"""Simple http echo server"""

import json

from flask import Flask, request, Response

_HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=_HTTP_METHODS)
@app.route('/<path:path>', methods=_HTTP_METHODS)
def catch_all(path: str) -> Response:
    """Catch-all method which handles all http requests.

    Args:
        path (str): The path string, not used.

    Returns:
        Response: A plain text Response echoing the contents of the user's original request
    """
    s = f"{request.method} {request.path}{'?' + request.query_string.decode() if request.query_string else ''}\n----\n{str(request.headers).strip()}\n----\n"

    if request.is_json:
        s += json.dumps(request.json, indent=4)
    elif request.form:
        s += "\n".join([f"{k} = {v}" for k, v in request.form.items()])
    elif request.files:
        s += "binary files were detected in body, obviously can't show them"
    elif request.data:
        s += str(request.data)

    return Response(s, mimetype='text/plain')


def _main() -> None:
    """Main method, invoked if this script is run directly"""
    app.run()


if __name__ == "__main__":
    _main()
