#!/usr/bin/env python

a = []
j = 0
end = 0

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

i = int(raw_input())

while i < len(a):
    if a[i] < a[j]:
        j = i
    i = i + 1

print j
