#!/bin/bash

if ! [[ -d ./.venv ]]; then
    python -m venv ./.venv
    pip install --upgrade pip
    if [[ -f ./requirements.txt ]]; then
        pip install -r ./requirements.txt
    fi
fi
