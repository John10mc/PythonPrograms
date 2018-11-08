#!/usr/bin/env python

i = 0
total = 0
while total != 1000:
    s = raw_input()
    j = 0
    while j < len(s) and s[j] != "+":
        j = j + 1
    total = int(s[0:j]) + int(s[j:])
    print total
    i = i + 1
