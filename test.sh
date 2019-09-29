#!/bin/bash

if [ "$1" = "-v" ]; then
  STDERR_FLAG=1
fi

for i in {01..99}; do
  if [ ! -f test/i${i}.txt ]; then
    exit
  fi

  if [ -z "$STDERR_FLAG" ]; then
    ACTUAL=`cargo run < test/i${i}.txt 2>/dev/null`
  else
    ACTUAL=`cargo run < test/i${i}.txt`
  fi
  EXPECTED=`cat test/o${i}.txt`

  echo "expected: $EXPECTED"
  echo "actual:   $ACTUAL"

  if [ "$ACTUAL" = "$EXPECTED" ]; then
    echo OK
  else
    echo NG
  fi
done
