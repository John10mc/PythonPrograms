#!/usr/bin/env python

s = ""
count = 0
while s != "end":
    s = raw_input()
    i = 0

    while i < len(s) - 1:
        if s[i] + s[i + 1] == "WI":
            name = s[0:i - 1]
            print name
        i = i + 1

print count
