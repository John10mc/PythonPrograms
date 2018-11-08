#!/usr/bin/env python

curr = input()

while curr != 0:
    prev = curr
    curr = input()

    if curr == 0:
        curr = 0
    elif curr < prev:
        print "lower"
    elif prev < curr:
        print "higher"
    else:
        print "equal"
