#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:21:07 2018

@author: matt
"""

def miniMaxSum(arr):
    curr_min = 1e10
    curr_max = 0
    l        = len(arr)
    for i in range(l):
        shifted = shift_seq(arr, i + 1)
        test    = sum(shifted[0:-1])
        if test < curr_min:
            curr_min = test
        if test > curr_max:
            curr_max = test
    print(curr_min, curr_max)
    
def shift_seq(arr, n):
    return arr[n::] + arr[:n]    
    
arr = [1, 2, 3, 4, 5]


miniMaxSum(arr)

#%%

arr = [1, 2, 3, 4, 5]
arr[2::] + arr[:2]

