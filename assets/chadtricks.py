#!/usr/bin/env python3
"""Chad Tricks!!"""
######clear screen from chad
from subprocess import call
from os import name as osname
#####print 1by1 dependencies
import sys, time

def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print

    ##Upgraded chad trick for animation
def video(arrayOfText,delay=0.5):
    for c in arrayOfText:
        clear()
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)


def clear():
    # check and make call for specific operating system
    call('clear' if osname =='posix' else 'cls')
