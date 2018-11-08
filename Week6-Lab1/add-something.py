#!/usr/bin/env python

a = []
s = raw_input()
i = 0

while s != "end":
    s = int(s)
    a.append(s)
    s = raw_input()

last = raw_input()

while i != len(a):
    add = 0
    add = a[i] + int(last)
    i = i + 1
    print add
