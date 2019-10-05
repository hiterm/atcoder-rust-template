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
    EXIT_CODE=$?
  else
    ACTUAL=`cargo run < test/i${i}.txt`
    EXIT_CODE=$?
  fi
  EXPECTED=`cat test/o${i}.txt`

  echo "expected: $EXPECTED"
  echo "actual:   $ACTUAL"

  if [ "$ACTUAL" = "$EXPECTED" ]; then
    if [ $EXIT_CODE -eq 0 ]; then
      echo OK
    else
      echo "exit code: $EXIT_CODE"
      echo NG
    fi
  else
    echo NG
  fi
done
