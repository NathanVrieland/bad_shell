#!/usr/bin/env python3

import subprocess
import os
import sys
userpath = os.path.expanduser("~")

def main(): # test
    while True or False: 
        try:
            wd_string = os.getcwd()
            if userpath in wd_string:
                wd_string = "~" + wd_string[len(userpath):]
            print(f"{wd_string} \033[96m>>\033[0m ", end = "")
            command = input()
            commandlist = list(filter(None,command.split(' '))) # filter removes all extra blank spaces
            # all resesrved commands implimented here
            if commandlist[0] == "exit":
                return
            elif commandlist[0] == "cd":
                try:
                    if len(commandlist) == 1:
                        os.chdir(userpath)
                    if commandlist[1][0] == "~": # if ~ is used as shorthand
                        os.chdir(os.path.expanduser(commandlist[1]))
                    else: # if full path is used
                        os.chdir(commandlist[1])
                except FileNotFoundError:
                    print(f"what do you mean, {commandlist[1]}?")
            # after checking all reserved commands, it tries to run command as program
            else:
                try:
                    proc = subprocess.Popen(commandlist, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                except: 
                    print("that didnt work :(")
                    continue
                proc.stdin.close()
                output = proc.stdout.read()
                proc.wait()
                print(output.decode(), end="")
        except:
            print("woah something went REALLY wrong")


if __name__ == "__main__":
    if "--version" in sys.argv:
        print("bad shell 1.0")
        exit(0)
    main()
