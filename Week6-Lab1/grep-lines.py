#!/usr/bin/env python

import sys
args = sys.argv
s = raw_input()


while s != "end":
    i = 0
    while i < len(s):
        if s[i:i + len(args[1])] == args[1]:
            print s
        i = i + 1
    s = raw_input()
