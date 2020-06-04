#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:37:42 2018

@author: matt
"""

import math
import os
import random
import re
import sys
import string
# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    lst = []
    alpha = string.ascii_lowercase
    for letter in word:
        idx = alpha.index(letter)
        lst.append(h[idx])
    return len(word)*max(lst)


test = 'abc'
h    = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
print(designerPdfViewer(h, test))