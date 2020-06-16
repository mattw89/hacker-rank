#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:56:10 2018

@author: matt
"""


import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colours = dict()
    for i in ar:
        if i in colours:
            colours[i] += 1
        else:
            colours[i] = 1
    pairs = 0
    for key in colours:       
        colours[key] = int(colours[key] / 2)
        pairs += colours[key]
    return pairs

n  = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20] 

print(sockMerchant(n, ar))
            
    