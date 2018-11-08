!/usr/bin/env python

a = input()
b = input()
c = input()

if b > a:
    temp = a
    b = a
    a = temp

 if c > a:
    temp = a
    c = a
    a = temp

add = b + c

if add < a:
    print "no"
else:
    print "yes"
