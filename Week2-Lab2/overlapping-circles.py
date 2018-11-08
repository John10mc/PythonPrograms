#!/usr/bin/env python

x1 = input()
y1 = input()
r1 = input()

x2 = input()
y2 = input()
r2 = input()

x1 = x2 - x1

y2 = y2 - y1

hyp = x1 ** 2 + y2 ** 2

if hyp <= r1 + r2:
    print "yes"
else:
    print "no"
