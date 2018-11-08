#!/usr/bin/env python

s = ""
name = ""
while s != "end":
    s = raw_input()
    i = 0

    while i < len(s) - 1:
        if s[i] == ":":
            name = s[0:i]
            i = len(s)
        i = i + 1
    print name
