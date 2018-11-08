#!/usr/bin/env python

n = input()

temp = n / 2

if n == 2:
    print "prime"
elif n >= 2 and n % 2 != 0 and temp * 2 == n:
    print "prime"
else:
    print "not prime"
