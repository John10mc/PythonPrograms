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
        line = a[i]
        line = int(line[6:8])
        line2 = a[j]
        line2 = int(line2[6:8])

        if line < line2:
            j = i
        i = i + 1
        
    temp = a[j]
    a[j] = a[0 + count]
    a[0 + count] = temp
    count = count + 1

i = 0
while i < len(a):
    line = a[i]
    line = line[9:]
    print line
    i = i + 1
