#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:46:12 2018

@author: matt
"""

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level  = 0
    valley = 0
    mount  = 0
    for step in s:
        if level < 0:
            pos = 'below'
        else:
            pos = 'above'
        if step == 'D':
            level -= 1
            if level == 0 and pos == 'above':
                mount += 1
        elif step == 'U':
            level += 1
            if level == 0 and pos == 'below':
                valley += 1
    #return level, valley, mount
    return valley

n = 12
s = 'DDUUDDUDUUUD'

print(countingValleys(n, s))