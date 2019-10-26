#!/bin/python

import sys
from pathlib import Path
import subprocess
import re
import argparse

# TODO -vvとかでverbose levelを設定？

def run_case(case, verbose_level):
    """
    Run one case.

    Parameters
    ----------
    case : str
        Case name. Both '01.txt' and '01' are accepted.
    verbose_level : int
        verbose level

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
        if verbose_level >= 1:
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

def run_all(verbose_level):
    """
    Run all cases.

    Parameters
    ----------
    verbose_level : int
        verbose level
    """
    ng_cases = []
    for file in sorted(Path('cases/in').iterdir()):
        if not file.is_file():
            continue

        if not run_case(file.name, verbose_level):
            ng_cases.append(file.name)
        print()

    if len(ng_cases) == 0:
        print("AC")
    else:
        print("NG cases: \n{}".format(" ".join(ng_cases)))


def run_selected(cases, verbose_level):
    """
    Run selected cases.

    Parameters
    ----------
    case : str[]
        list of cases
    verbose_level : int
        verbose level
    """

    ng_cases = []
    for case in cases:
        if not run_case(case, verbose_level):
            ng_cases.append(case)
        print()

    if len(ng_cases) == 0:
        print("AC")
    else:
        print("NG cases: \n{}".format(" ".join(ng_cases)))


parser = argparse.ArgumentParser()

parser.add_argument('cases', nargs='*')
parser.add_argument('--verbose', '-v', nargs='?', type=int, const=1, default=0)
args = parser.parse_args()

if len(args.cases) == 0:
    run_all(args.verbose)
else:
    run_selected(args.cases, args.verbose)
