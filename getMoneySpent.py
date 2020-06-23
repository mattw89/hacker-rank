#!/usr/bin/env python3
import os
import sys
#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    if min(keyboards) + min(drives) > b:
        return -1
    keyboards.sort(reverse = True)
    drives.sort(reverse    = True)
    print(keyboards, drives)
    total = 0
    for key in keyboards:
        for drive in drives:
            print(key, drive)
            if key + drive <= b and key + drive > total:
                total = key + drive
                #break
            

    return total


b = 10
n = 2
m = 3
keyboards = [3, 1]
drives    = [5, 2, 8]
print(getMoneySpent(keyboards, drives, b))


