#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:17:08 2018

@author: matt
"""

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    l     = len(s)
    count = 0
    for i in range(l):
        if (i + m) > l:
            break
        if sum(s[i: i + m]) == d: 
            count += 1
    return count


test = [1, 2, 1, 3, 2]
print(birthday(test, 3, 2))
        
