# http-echo-server
[![Python 3.11+](https://upload.wikimedia.org/wikipedia/commons/6/62/Blue_Python_3.11%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Simple HTTP echo server that responds back with whatver you sent it in plain text.  Intended as debugging/testing tool.

👉 The "echoed" body (if a body was included in the original request) will auto-format json and form data for legibility.

## Run
```bash
# from source
python -m http_echo

# prod
gunicorn -w 2 -b "0.0.0.0" http_echo.__main__:app
```