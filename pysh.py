#!/usr/bin/python3
import os
import sys
import getpass
import subprocess

USERNAME = getpass.getuser()
HOSTNAME = os.uname()[1]
DIR = os.getcwd()

PS=f"{USERNAME}@{HOSTNAME}:{DIR} # "

while True:
    try:
        cmd_input = input(PS)
        if cmd_input == "exit":
            sys.exit(0)
        os.system(cmd_input)
    except KeyboardInterrupt:
        print("^C")
