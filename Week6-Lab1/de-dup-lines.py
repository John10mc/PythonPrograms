#!/usr/bin/env python

a = []
s = raw_input()
i = 0

while s != "end":
    a.append(s)
    s = raw_input()

while i < len(a):
    j = i + 1
    while j < len(a):
        if a[i] == a[j]:
            a.pop(j)
        j = j + 1
    i = i + 1

i = 0

while i < len(a):
    j = i + 1
    while j < len(a):
        if a[i] == a[j]:
            a.pop(j)
        j = j + 1
    i = i + 1

i = 0

while i < len(a):
    print a[i]
    i = i + 1
