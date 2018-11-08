#!/usr/bin/env python

if __name__ == "__main__":
    a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
    s = "mont"

i = 0
while i < len(a):
    temp = a[i]
    if temp[:len(temp)] == s:
        print a[i]
    i = i + 1
