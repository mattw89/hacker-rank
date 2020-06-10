#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    distA = abs(z - x)
    distB = abs(z - y)
    if distA < distB:
        return 'Cat A'
    elif distB < distA:
        return 'Cat B'
    else:
        return 'Mouse C'


x = 1
y = 2
z = 3
print(catAndMouse(x, y, z))

