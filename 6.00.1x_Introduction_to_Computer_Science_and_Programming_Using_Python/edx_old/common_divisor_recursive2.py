# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 01:02:36 2016

@author: Camilo Cruz
"""

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)

print gcdRecur(0,6)