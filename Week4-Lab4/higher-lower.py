#!/usr/bin/env python

i = 0
curr = 0
prev = input()

while i < 5:
    curr = input()
    if curr < prev:
        print "lower"
    elif prev < curr:
        print "higher"
    else:
        print "equal"
    prev = curr
    i = i + 1
