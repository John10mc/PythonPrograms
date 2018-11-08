#!/usr/bin/env python

s = raw_input()
name = ""
while s != "end":
    s = raw_input()
    i = 0

    while i < len(s) - 4:
        if (s[i:i + 4]) == "City":
            name = s[0:i + 4]
            print name
        i = i + 1
