#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:15:15 2018

@author: matt
"""

def summingPieces(arr):
    length   = len(arr)
    start    = length - 2
    m_vec    = [0]*length
    s_vec    = [1]
    mod      = 1e9 + 7
    n        = (10**6) + 3
    for i in range(1, n):
        s_vec.append((s_vec[i-1] * 2) % mod)
    
    m_vec[0] = m_vec[-1] = (s_vec[length]-1+mod) % mod
    for i in range(1, (length // 2) + 1):
        m_vec[i]    = (s_vec[start] - s_vec[i-1]+mod) % mod
        m_vec[i]    = (m_vec[i-1] + m_vec[i]) % mod
        m_vec[-i-1] = m_vec[i]
        start      -= 1
    total = 0
    
    for i in range(length):
        total = (total + (m_vec[i] * ((arr[i]) % mod)) % mod) % mod
    
    return total
    

A2 = [4, 2, 9, 10, 1]
print(summingPieces(A2))    
    
    
#%%

if __name__ == '__main__':
    fptr = open('test.txt', 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


