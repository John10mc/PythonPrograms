#!/usr/bin/env python

s = raw_input()
i = 0

while i < len(s) and (s[i] <= "0" or "9" <= s[i]):
    i = i + 1
    j = i

while j < len(s) and not(s[j] <= "0" or "9" <= s[j]):
    j = j + 1

if i < len(s):
    print s[i:j], i
