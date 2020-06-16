#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    lst = []
    best = 0
    for i in range(len(a)):
        test = a[i::] + a[:i:]
        lst  = [abs(test[0] - test[j]) for j in range(1, len(test))]
        #print(test)
        print(lst)
        counter = lst.count(1) + lst.count(0)
        print(counter)
        print()
        if counter > best:
            best = counter
    return best


def pickingNumbers(a):
    # Write your code here
    best = 0
    for num in a:
        t1 = a.count(num)
        t2 = a.count(num-1)
        s  = t1 + t2
        if s > best:
            best = s
    return best 

# a = [4, 6, 5, 3, 3, 1]
# a = [98, 3, 99, 1, 97, 2]
# print(pickingNumbers(a))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
