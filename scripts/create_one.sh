#!/bin/bash

shopt -s extglob

if [ $# -ne 1 ]; then
  echo "One argument is required."
  exit
fi

DIR=$1
mkdir $DIR
cp -r template/!(cases|scripts|target) $DIR
cp -r template/.gitignore $DIR
