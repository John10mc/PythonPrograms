#!/usr/bin/env python

s = raw_input()
i = 0

while i < len(s) and (s[i] <= "0" or "9" <= s[i]):
    i = i + 1

if i < len(s):
    j = i
    while j < len(s) and not (s[j] <= "0" or "9" <= s[j]):
        j = j + 1

    if j < len(s):
        p = j
        while p < len(s) and (s[p] <= "0" or "9" <= s[p]):
            p = p + 1

        if p < len(s):
            m = p
            while m < len(s) and not (s[m] <= "0" or "9" <= s[m]):
                m = m + 1

            if m < len(s):
                print s[p - 1:m], p - 1
