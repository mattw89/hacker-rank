#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:42:35 2018

@author: matt
"""
import numpy as np
def aVeryBigSum(ar):
    total = 0
    for i in ar:
        total += i
    return total

# Test Case

ar  = np.array([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
ans = 5000000015

assert(ans == aVeryBigSum(ar))
print("Pass")

