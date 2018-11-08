#!/usr/bin/env python

a = input()
b = input()
c = input()

n_one = a + b
n_two = a + c
n_three = b + c

if n_one <= c or n_two <= b or n_three <= a:
    print "no"
else:
    print "yes"
