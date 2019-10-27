#!/bin/bash

if [ $# -ne 1 ]; then
  echo "One argument is required."
  exit
fi

DIRNAME=$1

mkdir $DIRNAME
for subdir in a b c d e f; do
  ./create_one.sh $DIRNAME/$subdir
done
