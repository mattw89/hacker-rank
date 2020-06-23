#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:44:25 2018

@author: matt
"""

def staircase(n):
    for i in range(n):
        has      = '#'
        space    = ' '
        line_msg = (n - (i + 1))*space + (i + 1)*has
        print(line_msg)
    return None


staircase(6)

