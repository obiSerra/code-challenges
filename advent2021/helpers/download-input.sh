#!/bin/bash

if [ "$1" = "" ]; then
    echo "USAGE: $ download-input.sh <day-num>"
    exit
fi

year="2021"

baseurl="https://adventofcode.com/$year/day/$1/input"
session=`cat "./session_cookie"`

if [ "$session" = "" ]; then
    echo "ERROR: Session_cookie is empty"
    exit
fi

curl -v --cookie "session=$session" $baseurl --output "day-$1/input.txt"