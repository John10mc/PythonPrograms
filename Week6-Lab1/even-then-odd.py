#!/usr/bin/env python

a = []
s = raw_input()
i = 0

while s != "end":
    s = int(s)
    a.append(s)
    s = raw_input()

while i != len(a):
    if int(a[i]) % 2 == 0:
        print int(a[i])
    i = i + 1

i = 0

while i != len(a):
    if int(a[i]) % 2 != 0:
        print int(a[i])
    i = i + 1

