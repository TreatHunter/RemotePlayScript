#! /usr/bin/python3

"""
https://github.com/TreatHunter
This is remote play script. Its purpose is to control old pc as tvstation to be controlled over ssh
v2.1.0

MIT License

Copyright (c) 2024 TreatHunter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import subprocess
import sys
import time


class Commands():
    apCommand = "ap"
    rtnCommand = "rtn"
    returnCommand = "return"
    exitCommand = "exit"


def help():
    print()
    print("<>")
    print("Commands:")
    print(Commands.apCommand + " - play link in new anonymous tab")
    print(Commands.rtnCommand + " or " + Commands.returnCommand + " - return back")
    print(Commands.exitCommand + " - exit the program (works everywhere)")
    print("<>")
    print()

def ap(uInput):
    subprocess.run("xdotool getactivewindow key ctrl+w", shell=True, executable="/bin/bash")
    subprocess.run(" nohup firefox --private-window " + uInput + "&", shell=True, executable="/bin/bash")
    time.sleep(20)
    subprocess.run("xdotool getactivewindow key f", shell=True, executable="/bin/bash")


def apInteractiveMode():
    print("anonymous play")
    while True:
        uInput = input("enter link to open or command: ")
        match uInput:
            case Commands.rtnCommand | Commands.returnCommand:
                break
            case "exit":
                exit(0)
            case _:
                ap(uInput)


def interactiveMode():
    print("Welcome to python remote play")
    while True:
        help()
        command = input("enter regime of work: ")
        match command:
            case Commands.apCommand:
                apInteractiveMode()
            case Commands.rtnCommand | Commands.returnCommand:
                continue
            case Commands.exitCommand:
                exit(0)
            case _:
                print("unknown command")

def executeMode():
    match sys.argv[1]:
        case Commands.apCommand:
            ap(sys.argv[2])
        case _:
            print("unknown command")
            exit(1)

os.environ["DISPLAY"] = ":0"
if len(sys.argv) == 1:
    interactiveMode()
    exit(0)
else:
    executeMode()
