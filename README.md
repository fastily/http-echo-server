# http-echo-server
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Simple HTTP echo server that responds back with whatver you sent it in plain text.  Intended as debugging/testing tool.

👉 The "echoed" body (if a body was included in the original request) will auto-format json and form data for legibility.

## Usage
```bash
# install dependencies
uv sync --no-install-project

# start in development mode, available at http://127.0.0.1:5000
uv run python -m http_echo_server

# run w/ gunicorn, accessible at localhost:8000
uv run gunicorn -w 2 -b "0.0.0.0" --access-logfile "-" --no-control-socket http_echo_server.__main__:app
```