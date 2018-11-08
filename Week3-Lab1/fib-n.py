#!/usr/bin/env python

n = input()

curr = 0
prev = 1

i = 0
while i < n:
    print curr
    old = curr
    curr = curr + prev
    prev = old

    i = i + 1
