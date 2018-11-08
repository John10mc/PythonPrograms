#!/usr/bin/env python

a = []
j = 0
end = 0
i = 0
count = 0
s = raw_input()

while s != "end":
    a.append(s)
    s = raw_input()

while count < len(a):
    i = 0 + count
    j = 0 + count
    while i < len(a):
        if a[i] < a[j]:
            j = i
        i = i + 1
    temp = a[j]
    a[j] = a[0 + count]
    a[0 + count] = temp
    count = count + 1

i = 0
while i < len(a):
    print a[i]
    i = i + 1
