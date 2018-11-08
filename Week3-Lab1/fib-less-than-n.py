#!/usr/bin/env python

n = input()

curr = 0
prev = 1

i = 0
while curr < n:
    print curr
    old = curr
    curr = curr + prev
    prev = old
