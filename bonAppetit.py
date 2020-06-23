#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:14:00 2018

@author: Matt
"""

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    if k == 0:
        total  = sum(bill)/2
        charge = abs(total - b)
        if charge == 0:
            print('Bon Appetit')
        else:
            print(int(charge))
    else:
        total = (sum(bill[0:k]) + sum(bill[k + 1::]))/2
        #print(bill[0:k])
        #print(bill[k + 1::])
        charge = abs(total - b)
        if charge == 0:
            print('Bon Appetit')
        else:
            print(int(charge))
            
            
bill = [3, 10, 2, 9]
k    = 1
b    = 12

print(bonAppetit(bill, k, b))
        
        
        
        
        
        
        
