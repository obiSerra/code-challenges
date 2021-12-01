#!/bin/bash

if [ "$1" = "" ]; then
    echo "USAGE: $ new-day.sh <day-num>"
    exit
fi

mkdir "day-$1"

FILE_CONTENT="from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input.txt')

# with open(final_path) as file:
#     lines = file.readlines()
#     input = [line.rstrip() for line in lines]

def solution(input):
    pass


if __name__ == '__main__':
    print(solution(input))"


echo "$FILE_CONTENT" > "day-$1/star.py"
echo "$FILE_CONTENT" > "day-$1/star2.py"

source ./helpers/download-input.sh $1