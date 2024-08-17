#!/bin/usr/env bash
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python not installed"
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "ERROR: pip not installed"
    exit 1
fi


git submodule init
git submodule update
pip install -r requirements.txt

