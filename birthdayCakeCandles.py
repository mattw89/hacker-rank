#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:50:02 2018

@author: matt
"""

def birthdayCakeCandles(ar):
    max_height = max(ar)
    candles    = 0
    for i in ar:
        if i == max_height:
            candles += 1
    print(candles)
    
ar = [3, 2, 1, 3]
birthdayCakeCandles(ar)    