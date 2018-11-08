#!/usr/bin/env python

a = []
s = raw_input()
i = 0

while s != "end":
    a.append(s)
    s = raw_input()

while i < len(a):
    print i, len(a), a[i]
    i = i + 1
