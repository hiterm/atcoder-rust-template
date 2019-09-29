#!/bin/bash

for i in {01..99}; do
  if [ ! -f test/i${i}.txt ]; then
    exit
  fi

  ACTUAL=`cargo run < test/i${i}.txt`
  EXPECTED=`cat test/o${i}.txt`

  if [ "$ACTUAL" = "$EXPECTED" ]; then
    echo OK
  else
    echo NG
  fi
done
