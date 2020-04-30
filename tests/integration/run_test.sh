#!/usr/bin/env bash

pip3 install dogtail

RUN_DIR=$(dirname $(realpath "$0"))
xvfb-run -a python3 "${RUN_DIR}/run_app.py" nicotine