#!/usr/bin/env python

s_one = raw_input()
s_two = raw_input()
s_three = raw_input()

if len(s_one) > len(s_two) and len(s_one) > len(s_three):
    print s_one
elif len(s_two) > len(s_one) and len(s_two) > len(s_three):
    print s_two
else:
    print s_three
