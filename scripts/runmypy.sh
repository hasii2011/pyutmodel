#!/usr/bin/env bash

function changeToProjectRoot {

    export areHere=`basename ${PWD}`
    if [[ ${areHere} = "scripts" ]]; then
        cd ..x``
    fi
}

changeToProjectRoot

mypy --config-file .mypi.ini --pretty --no-color-output --show-error-codes pyutmodel
# mypy --config-file .mypi.ini --pretty  --show-error-codes pyutplugincore tests
status=$?

echo "Exit with status: ${status}"
exit ${status}

