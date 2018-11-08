#!/usr/bin/env python

i = 0
s = raw_input()
total = 0
j = 0

while i < len(s):

    while j < len(s) and s[j] != "+":
        j = j + 1
        total = s[i:j]

    i = i + 1
    i = j


print total