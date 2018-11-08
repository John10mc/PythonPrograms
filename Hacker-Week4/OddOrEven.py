#!/usr/bin/env python

n = input()
i = 0

while i < n:
    t = input()
    if t % 2 == 0:
        print str(t) + " is even"
    else:
        print str(t) + " is odd"
    i = i + 1