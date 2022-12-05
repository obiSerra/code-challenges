#!/bin/bash

if [ "$1" = "" ]; then
    echo "USAGE: $ new-day.sh <day-num>"
    exit
fi

mkdir "day-$1"

FILE_CONTENT="from os import path

input = []

final_path = path.join(path.dirname(path.abspath(__file__)),
                       'input_test.txt')

with open(final_path) as file:
    lines = file.readlines()
    input = [line.strip() for line in lines]

def solution(input):
    return input


if __name__ == '__main__':
    print(solution(input))"


echo "$FILE_CONTENT" > "day-$1/star.py"
echo "$FILE_CONTENT" > "day-$1/star2.py"

touch "day-$1/input_test.txt"

source ./helpers/download-input.sh $1