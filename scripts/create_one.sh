#!/bin/bash

shopt -s extglob

if [ $# -ne 1 ]; then
  echo "One argument is required."
  exit
fi

SCRIPT_DIR=$(dirname $0)

DIR=$1
mkdir -p $DIR
cp -r $SCRIPT_DIR/template/{src,Cargo.toml,.gitignore} $DIR
