#!/bin/bash

if [ "$1" = "-v" ]; then
  STDERR_FLAG=1
fi

for file in $(ls cases/in); do
  infile="cases/in/$file"
  outfile="cases/out/$file"
  if [ ! -f "$outfile" ]; then
    echo "$outfile not found"
    exit
  fi

  if [ -z "$STDERR_FLAG" ]; then
    ACTUAL=`cargo run < $infile 2>/dev/null`
    EXIT_CODE=$?
  else
    ACTUAL=`cargo run < $infile`
    EXIT_CODE=$?
  fi
  EXPECTED=`cat $outfile`

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
