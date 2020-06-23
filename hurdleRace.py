#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:50:52 2018

@author: matt
"""


import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    return max(max(height) - k, 0)

height = [1, 6, 3, 5, 2]
k = 4

print(hurdleRace(k, height))