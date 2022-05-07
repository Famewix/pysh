#!/usr/bin/python3
import os
import sys
import getpass
import subprocess

def get_current_dir():
    if os.getcwd() == os.path.expanduser('~'):
        return "~"
    else:
        return os.getcwd()

USERNAME = getpass.getuser()
HOSTNAME = os.uname()[1]
DIR = get_current_dir()


while True:
    try:
        PS=f"{USERNAME}@{HOSTNAME}:{DIR} # "
        cmd_input = input(PS)
        if cmd_input == "exit":
            sys.exit(0)
        elif cmd_input.split(" ")[0] == "cd":
            if cmd_input == "cd":
                os.chdir(os.path.expanduser('~'))
            else:
                os.chdir(cmd_input.split(' ')[-1])
            DIR = get_current_dir()
        os.system(cmd_input)
    except KeyboardInterrupt:
        print("^C")
