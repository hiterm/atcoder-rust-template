#!/bin/python

import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('problem')
parser.add_argument('--bin', action='store_true')
parser.add_argument('--force', action='store_true')
parser.add_argument('--release', action='store_true')
args = parser.parse_args()

problem = args.problem

# detect debug prints
file = 'src/bin/{}.rs'.format(problem)
p1 = subprocess.Popen(['grep', '-e', 'eprintln!', '-e', 'dbg!', file],
                      stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', '-v', '^ *//'],
                      stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0].decode()
if output != "":
    print()
    print("!!!!Please remove debug prints!!!!")
    print(output)
    sys.exit()

# detect todo comments
output = subprocess.run(['grep', 'TODO', file], stdout=subprocess.PIPE).stdout.decode()
if output != "":
    print()
    print("!!!!Please check TODO comments!!!!")
    print(output)
    sys.exit()

commands = ['cargo', 'compete', 'submit', problem]
if args.bin:
    commands.append('--bin')
if args.force:
    commands.append('--no-test')
if args.release:
    commands.append('--release')
subprocess.run(
    commands
)
