#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:22:15 2018

@author: matt
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    house        = list(range(s, t + 1))
    apple_count  = 0
    orange_count = 0
    for apple in apples:
        if (a + apple) in house:
            apple_count += 1
    for orange in oranges:
        if (b + orange) in house:
            orange_count += 1
    print(apple_count)
    print(orange_count)
    #return apple_count, orange_count



# Test case

s = 7
t = 10
a = 4
b = 12
apples  = [2, 3, -4]
oranges = [3, -2, -4] 


print(countApplesAndOranges(s, t, a, b, apples, oranges))



#%% 

# Apparently the above is too slow so this instead:

def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))