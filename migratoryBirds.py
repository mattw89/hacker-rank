#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:38:21 2018

@author: matt
"""

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birds = dict()
    for bird in arr:
        #print(bird)
        if bird not in birds:
            birds[bird] = 1
        else:
            birds[bird] += 1
    maximum  = max(birds, key=birds.get)  
    smallest = maximum
    for bird in birds:
        if birds[bird] == birds[maximum] and bird < maximum:
            smallest = bird
    
    return smallest



test = [1, 4, 4, 4, 5, 3]

print(migratoryBirds(test))