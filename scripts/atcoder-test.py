#!/bin/python

import sys
from pathlib import Path
import subprocess
import re

# TODO -vvとかでverbose levelを設定？
# 最後に間違ったやつの一覧

def run_case(case, flag_stderr):
    """
    Run one case.

    Parameters
    ----------
    case : str
        Case name. Both '01.txt' and '01' are accepted.
    flag_stderr : bool
        flag for show stderr

    Returns
    -------
    accepted : bool
        whether accepted or not
    """
    if re.match(r'.*\.txt', case):
        infile_path = Path('cases/in') / case
        outfile_path = Path('cases/out') / case
    else:
        infile_path = Path('cases/in') / (case + '.txt')
        outfile_path = Path('cases/out') / (case + '.txt')

    if not outfile_path.exists():
        print('{} not found.'.format(outfile_path))
        return False

    # run case
    infile = infile_path.open()
    try:
        if flag_stderr:
            result = subprocess.run(['rustup', 'run', '1.15.1', 'cargo', 'run'], stdin=infile, stdout=subprocess.PIPE, timeout=3)
        else:
            result = subprocess.run(['rustup', 'run', '1.15.1', 'cargo', 'run'], stdin=infile, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=3)
        actual = result.stdout.decode().rstrip()
    except subprocess.TimeoutExpired:
        print("{}: TLE".format(infile_path.name))
        return False

    expected = outfile_path.open().read().rstrip()

    # check result
    if result.returncode != 0:
        accepted = False
        result_type = "RE, Exit Code: {}".format(result.returncode)
    elif actual == expected:
        accepted = True
        result_type = "AC"
    else:
        accepted = False
        result_type = "WA"

    print("{}: {}".format(infile_path.name, result_type))

    infile.seek(0)
    print('INPUT:    \n{}'.format(infile.read().rstrip()))
    print('EXPECTED: "{}"'.format(expected))
    print('ACTUAL:   "{}"'.format(actual))

    return accepted

def run_all(flag_stderr):
    """
    Run all cases.

    Parameters
    ----------
    flag_stderr : bool
        flag for show stderr
    """
    ng_cases = []
    for file in sorted(Path('cases/in').iterdir()):
        if not file.is_file():
            continue

        if not run_case(file.name, flag_stderr):
            ng_cases.append(file.name)
        print()

    if len(ng_cases) == 0:
        print("AC")
    else:
        print("NG cases: \n{}".format(" ".join(ng_cases)))


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

    ng_cases = []
    for case in cases:
        if not run_case(case, flag_stderr):
            ng_cases.append(case)
        print()

    if len(ng_cases) == 0:
        print("AC")
    else:
        print("NG cases: \n{}".format(" ".join(ng_cases)))


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
