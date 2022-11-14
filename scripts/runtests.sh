#!/usr/bin/env bash

function changeToProjectRoot {

    areHere=$(basename "${PWD}")
    export areHere
    if [[ ${areHere} = "scripts" ]]; then
        cd ..
    fi

    if [[ ${areHere} = "src" ]]; then
        cd ..
    fi
}

function checkStatus {

    status=$1
    testName=$2

    echo "checkStatus ${testName} -- ${status}"
    if [ "${status}" -ne 0 ]
    then
        exit "${status}"
    fi
}

changeToProjectRoot

echo "Travis Build directory: ${TRAVIS_BUILD_DIR}"

python3 -m tests.TestAll
status=$?

cd - > /dev/null 2>&1  || ! echo "No such directory"

# ./scripts/cleanup.sh

echo "Exit with status: ${status}"
exit "${status}"
