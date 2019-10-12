#!/bin/python

import sys
from pathlib import Path
import subprocess

stderr_flag = (len(sys.argv) >= 2 and sys.argv[1] == "-v")

for file in sorted(Path('cases/in').iterdir()):
    if not file.is_file():
        continue

    infile_path = file
    outfile_path = Path('cases/out') / file.name

    if not outfile_path.exists():
        print('{} not found.'.format(outfile_path))
        continue

    # run cases
    infile = infile_path.open()
    try:
        if stderr_flag:
            result = subprocess.run(['cargo', 'run'], stdin=infile, stdout=subprocess.PIPE, timeout=3)
        else:
            result = subprocess.run(['cargo', 'run'], stdin=infile, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=3)
        actual = result.stdout.decode().rstrip()
    except subprocess.TimeoutExpired:
        print("{}: NG".format(infile_path.name))
        print("TLE")
        continue

    expected = outfile_path.open().read().rstrip()

    # check result
    if result.returncode != 0:
        print("{}: NG".format(infile_path.name))
        print("Exit code: {}".format(result.returncode))
    elif actual == expected:
        print("{}: OK".format(infile_path.name))
    else:
        print("{}: NG".format(infile_path.name))
    print('EXPECTED: "{}"'.format(expected))
    print('ACTUAL:   "{}"'.format(actual))
