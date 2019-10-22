#!/bin/bash

shopt -s extglob

if [ $# -ne 1 ]; then
  echo "One argument is required."
  exit
fi

DIR=$1
mkdir $DIR
cp -r template/{src,Cargo.toml,.gitignore} $DIR
