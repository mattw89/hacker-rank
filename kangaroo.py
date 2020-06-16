#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:03:37 2018

@author: matt
"""


import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return 'NO'
    while True:
        if x1 == x2:
            return 'YES'
        x1 += v1
        
#        if x1 == x2:
#            return 'YES'
        
        x2 += v2
        if x1 and x2 > 10000000:
            return 'NO'

x1 = 1571
v1 = 4240
x2 = 9023
v2 = 4234

#x1 = 28
#v1 = 8
#x2 = 96
#v2 = 2

#x1 = 0
#v1 = 3
#x2 = 4
#v2 = 2

print(kangaroo(x1, v1, x2, v2))


#%%

def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return 'NO'
    
    #i = 1
    for i in range(10000):
        if (x1 + i*v1) == (x2 + i*v2):
            return 'YES'
            
    return 'NO'
    
x1 = 1571
v1 = 4240
x2 = 9023
v2 = 4234

print(kangaroo(x1, v1, x2, v2))