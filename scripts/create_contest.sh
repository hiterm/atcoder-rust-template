#!/bin/bash

if [ $# -ne 1 ]; then
  echo "One argument is required."
  exit
fi

SCRIPT_DIR=$(dirname "$0")

DIRNAME=$1

mkdir "$DIRNAME"
cp -r "$SCRIPT_DIR/template/"{src,Cargo.toml,.gitignore} "$DIRNAME"
for file in b c d e f; do
  cp "$DIRNAME/src/bin/a.rs" "$DIRNAME/src/bin/${file}.rs"
done
