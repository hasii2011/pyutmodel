#!/usr/bin/env bash

function changeToProjectRoot {

    export areHere=`basename ${PWD}`
    if [[ ${areHere} = "scripts" ]]; then
        cd ..
    fi
}

changeToProjectRoot

rm -rf dist build

find . -type d -name '*'.egg-info -delete

rm -rf .eggs
rm -rf pyutmodel.egg-info
