#!/usr/bin/env python

total = 0
n = input()

while n != 0:
    if n < 0:
        neg = neg + n
    else:
        pos = pos + n
    n = input()
    
print neg, pos
