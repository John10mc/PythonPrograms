#!/usr/bin/env python

n = input()
total = ""

while 0 < n:
    if n % 2 == 0:
        total = total + "0"
        n = n / 2
    else:
        total = total + "1"
        n = n / 2

t = ""
j = 0
while j < len(total):
    t = t + total[len(total) - j - 1]
    j = j + 1

print t
