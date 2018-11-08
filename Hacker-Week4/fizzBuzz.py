#!/usr/bin/env python

fizz = input()
buzz = input()
n = input()
i = 0

while i < n:
    if (i + 1) % fizz == 0 and (i + 1) % buzz == 0:
        print "fizz-buzz"
    elif (i + 1) % fizz == 0:
        print "fizz"
    elif (i + 1) % buzz == 0:
        print "buzz"
    else:
        print i + 1
    i = i + 1