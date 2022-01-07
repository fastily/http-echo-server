# http-echo-server
[![Python 3.9+](https://upload.wikimedia.org/wikipedia/commons/4/4f/Blue_Python_3.9%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Simple HTTP echo server that responds back with whatver you sent it in plain text.  Intended as debugging/testing tool.

👉 The "echoed" body (if a body was included in the original request) will auto-format json and form data for legibility.

## Run
```bash
# from source
python -m http_echo

# if installed as a package
http_echo_server
```