#!/usr/bin/env python

i = 0
s = raw_input()
total = 0
first = 0
second = 0

while i < len(s) and s[i] != "+":
    i = i + 1
    first = s[0:i]
    j = i + 1


    while j < len(s) and s[j] != "+":
        j = j + 1
        second = s[i + 1:j]


print int(first) + int(second)