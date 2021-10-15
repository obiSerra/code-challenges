#!/bin/bash

if [ "$1" = "" ]; then
    echo "USAGE: $ new-day.sh <day-num>"
    exit
fi

mkdir "day-$1"
touch "day-$1/silver-star.js"
touch "day-$1/gold-star.js"

source ./helpers/download-input.sh $1