#!/bin/python

import sys
from pathlib import Path
import subprocess
import re

// TODO inputも出力する
// -vvとかでverbose levelを設定？
// 最後に間違ったやつの一覧

def run_case(case, flag_stderr):
    """
    Run one case.

    Parameters
    ----------
    case : str
        Case name. Both '01.txt' and '01' are accepted.
    flag_stderr : bool
        flag for show stderr
    """
    if re.match(r'.*\.txt', case):
        infile_path = Path('cases/in') / case
        outfile_path = Path('cases/out') / case
    else:
        infile_path = Path('cases/in') / (case + '.txt')
        outfile_path = Path('cases/out') / (case + '.txt')

    if not outfile_path.exists():
        print('{} not found.'.format(outfile_path))
        return

    # run cases
    infile = infile_path.open()
    try:
        if flag_stderr:
            result = subprocess.run(['cargo', 'run'], stdin=infile, stdout=subprocess.PIPE, timeout=3)
        else:
            result = subprocess.run(['cargo', 'run'], stdin=infile, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=3)
        actual = result.stdout.decode().rstrip()
    except subprocess.TimeoutExpired:
        print("{}: NG".format(infile_path.name))
        print("TLE")
        return

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

def run_all(flag_stderr):
    """
    Run all cases.

    Parameters
    ----------
    flag_stderr : bool
        flag for show stderr
    """
    for file in sorted(Path('cases/in').iterdir()):
        if not file.is_file():
            continue

        run_case(file.name, flag_stderr)


def run_selected(cases, flag_stderr):
    """
    Run selected cases.

    Parameters
    ----------
    case : str[]
        list of cases
    flag_stderr : bool
        flag for show stderr
    """
    for case in cases:
        run_case(case, flag_stderr)


flag_stderr = False
flag_all = True
cases = []
if len(sys.argv) <= 1:
    pass
elif len(sys.argv) == 2 and sys.argv[1] == '-v':
    flag_stderr = True
else:
    flag_all = False
    for arg in sys.argv[1:]:
        if arg == '-v':
            flag_stderr = True
        else:
            cases.append(arg)

if flag_all:
    run_all(flag_stderr)
else:
    run_selected(cases, flag_stderr)
