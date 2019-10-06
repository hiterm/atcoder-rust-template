#!/bin/bash

if [ $# -ne 1 ]; then
  echo "One argument is required."
  exit
fi

DIRNAME=$1

mkdir $DIRNAME
for subdir in a b c d e f; do
  mkdir $DIRNAME/$subdir
  cp -r template/* $DIRNAME/$subdir
done

cd $DIRNAME
git init
git add -A
git commit -m "First commit"
