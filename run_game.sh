#!/bin/bash

if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 hangman1_main.py
    else
        echo "Please install Python 3.10 or later" >&2
    fi
fi

