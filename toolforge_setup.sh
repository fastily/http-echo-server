#!/usr/bin/env bash

toolforge build start "https://github.com/fastily/http-echo-server.git"
toolforge webservice buildservice start --mount=none