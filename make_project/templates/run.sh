#!/bin/bash

DIR="$PWD"
ACTIVATE=".venv/bin/activate"

if [[ -f "$ACTIVATE" ]]; then
    source $ACTIVATE
    echo -e "[\033[94m${VIRTUAL_ENV_PROMPT}\033[0m]"
    echo ""
else
    echo "[NO-VENV]"
    echo ""
fi

if [[ -f $DIR/"__main__.py" ]]; then
    # echo "------------------------------[BEGIN]------------------------------"
    echo ""
    python $DIR/"__main__.py" $@
    echo ""
    # echo "-------------------------------[END]-------------------------------"
fi

echo ""
