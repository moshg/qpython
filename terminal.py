from os import chdir
import os.path, sys, subprocess, readline


while(True):
    cmd=input('')
    if not cmd: break;
    try:
        subprocess.run(cmd.split())
    except FileNotFoundError as e:
        print(e)
