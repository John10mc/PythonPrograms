#!/usr/bin/env python

s = raw_input()
i = 0
out = ""
if len(s) == 1:
    out = "no hiss"

while i < len(s) - 1:
    if s[i] == "s" and s[i + 1] == "s":
        out =  "hiss"
        i = len(s) + 1
    else:
        out = "no hiss"
    i = i + 1
print out