#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:01:15 2018

@author: matt
"""

import math
import os
import random
import re
import sys
import numpy as np

def diagonalDifference(arr):
    arr = np.asarray(arr)
    d1  = sum(np.diag(arr)) 
    d2  = sum(np.diag(arr[:, ::-1]))   
    return abs(d1 - d2)

    
# Can't use numpy it seems    

#%%
    
test =  [[11, 2,   4],
         [4,  5,   6],
         [10, 8, -12]]

t = np.asarray(test)
print(np.diag(t))
print(t[:, ::-1])

print(diagonalDifference(test))




#%%

# No numpy
def diagonalDifference(arr):
    r  = len(arr)
    c  = len(arr[0])
    d1 = 0
    d2 = 0
    for i in range(r):
        d1 += arr[i][i]
        d2 += arr[i][((c - 1) - i)]
    return abs(d2 - d1)

#%%
    
test =  [[11, 2,   4],
         [4,  5,   6],
         [10, 8, -12]]

print(diagonalDifference(test))