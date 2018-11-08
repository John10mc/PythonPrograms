#!/usr/bin/env python

a = []
i = 0

while i < 3:
    n = input()
    a.append(n)
    i = i + 1

if a[0] > a[2]:
    temp = a[0]
    a[0] = a[2]
    a[2] = temp

if a[0] > a[1]:
    temp = a[0]
    a[0] = a[1]
    a[1] = temp

if a[1] > a[2]:
    temp = a[1]
    a[1] = a[2]
    a[2] = temp

i = 0
while i < 3:
    print a[i]
    i = i + 1
