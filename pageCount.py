#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:28:24 2018

@author: Matt
"""

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    lbest = 0
    rbest = 0
    if p == 1:
        return 0
    elif (p == n or p == n - 1) and n % 2 == 1:
        return 0
    elif (p == n - 1) and n % 2 == 0:
        return 1
    else:
        lbest = p // 2
        rbest = ((n - p) // 2)
    return min(lbest, rbest)
    #


n = 5
p = 4

print(pageCount(n, p))
        
