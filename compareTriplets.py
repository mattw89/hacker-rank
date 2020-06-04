#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:28:39 2018

@author: matt
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob   = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif b[i] > a[i]:
            bob += 1
    return (alice, bob)
    
   
a = [4, 8, 34]
b = [1, 21, 17]

compareTriplets(a, b)    
    
#%%   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


