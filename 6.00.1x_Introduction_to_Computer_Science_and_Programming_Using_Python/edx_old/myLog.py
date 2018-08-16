# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:54:15 2017

@author: Camilo Cruz
"""

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x <= b:
        return 1
    
    else: return myLog(x/b,b)+1

print myLog(16,2)