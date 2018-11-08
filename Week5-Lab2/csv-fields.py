#!/usr/bin/env python

s = raw_input()
field = ""
i = 0
j = 0

while i < len(s):
    while i < len(s) and s[i] != ",":
        field = s[j:i + 1]
        i = i + 1
    print field
    i = i + 1
    j = i
